# backend/projects/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView , FormView
from .forms import ContactForm




class HomeView(TemplateView):
    template_name = 'home.html'

# View para listar todos os projetos publicados
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        # Mostra apenas os projetos que estão marcados como "publicados"
        return Project.objects.filter(is_published=True)

# View para mostrar os detalhes de um único projeto
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    # Usa o 'slug' (texto-amigavel-para-url) em vez do ID do projeto
    slug_url_kwarg = 'slug'

# View para o formulário de criação de projeto (o "Painel do Criador")
# Garante que apenas usuários logados podem acessar
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    # Redireciona para a página inicial após criar um projeto com sucesso
    success_url = reverse_lazy('projects:list')
    # Se o usuário não estiver logado, redireciona para a tela de login do admin
    login_url = '/admin/login/'

class AboutView(TemplateView):
    template_name = "about.html"

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    login_url = '/admin/login/'

    def get_success_url(self):
        return reverse_lazy('projects:detail', kwargs={'slug': self.object.slug})

    # --- MÉTODO ADICIONADO (idêntico ao da CreateView) ---
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['drafts'] = Project.objects.filter(is_published=False).order_by('-created_at')
        return context

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:list') # Após excluir, volta para a lista
    login_url = '/admin/login/'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:list')
    login_url = '/admin/login/'

    # --- MÉTODO ADICIONADO ---
    def get_context_data(self, **kwargs):
        # Primeiro, pega o contexto que a view já gera (que inclui o formulário)
        context = super().get_context_data(**kwargs)
        
        # Agora, fazemos uma busca no banco de dados por todos os projetos
        # onde 'is_published' é Falso e os ordenamos pelos mais recentes.
        context['drafts'] = Project.objects.filter(is_published=False).order_by('-created_at')
        
        # Retornamos o contexto, agora com a nossa lista de rascunhos ('drafts')
        return context
    
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact') # Para onde ir após o envio com sucesso

    def form_valid(self, form):
        # Esta função é chamada quando o formulário é válido
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        # Monta a mensagem do email
        full_message = f"""
        Mensagem recebida de: {first_name} {last_name} ({email})
        ---
        {message}
        """

        # Envia o email
        send_mail(
            subject=f'Nova Mensagem do Portfólio de {first_name}',
            message=full_message,
            from_email=None,  # Usa o EMAIL_HOST_USER do settings.py
            recipient_list=['jeanrufinolima2004@gmail.com'], # Seu email de destino
        )

        # Adiciona uma mensagem de sucesso para o usuário
        messages.success(self.request, 'Sua mensagem foi enviada com sucesso! Obrigado por entrar em contato.')
        
        return super().form_valid(form)