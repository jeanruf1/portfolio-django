# backend/projects/forms.py
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # GARANTA QUE 'is_published' ESTEJA NESTA LISTA
        fields = [
            'title', 'cover', 'description', 'tech_details', 
            'video_url', 'video_file', 'github_url', 
            'is_published'
        ]
        labels = {
            'title': 'Título do Projeto',
            'cover': 'Imagem de Capa',
            'description': 'Descrição Detalhada',
            'tech_details': 'Tecnologias Usadas',
            'video_url': 'URL do Vídeo de Demonstração',
            'video_file': 'Ou Envie um Arquivo de Vídeo (MP4)',
            'github_url': 'Repositório no GitHub',
            'is_published': 'Publicar imediatamente?', # O label para a nossa checkbox
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'description': forms.Textarea(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 h-40 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'tech_details': forms.TextInput(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'video_url': forms.URLInput(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'github_url': forms.URLInput(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'cover': forms.ClearableFileInput(attrs={'class': 'hidden'}),
            'video_file': forms.ClearableFileInput(attrs={'class': 'hidden'}),
            # O widget para a checkbox que será estilizado no template
            'is_published': forms.CheckboxInput(attrs={'class': 'sr-only peer'}),
        }
    class Meta:
        model = Project
        fields = [
            'title', 'cover', 'description', 'tech_details', 
            'video_url', 'video_file', 'github_url', 
            'is_published'
        ]
        labels = {
            'title': 'Título do Projeto',
            'cover': 'Imagem de Capa',
            'description': 'Descrição Detalhada',
            'tech_details': 'Tecnologias Usadas',
            'video_url': 'URL do Vídeo de Demonstração',
            'video_file': 'Ou Envie um Arquivo de Vídeo (MP4)',
            'github_url': 'Repositório no GitHub',
            'is_published': 'Publicar imediatamente?',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'description': forms.Textarea(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 h-40 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'tech_details': forms.TextInput(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'video_url': forms.URLInput(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'github_url': forms.URLInput(attrs={'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400'}),
            'cover': forms.ClearableFileInput(attrs={'class': 'hidden'}), # Apenas para referência, o estilo está no HTML
            'video_file': forms.ClearableFileInput(attrs={'class': 'hidden'}), # Apenas para referência, o estilo está no HTML
            'is_published': forms.CheckboxInput(attrs={'class': 'sr-only peer'}), # Apenas para referência, o estilo está no HTML
        }

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Primeiro Nome")
    last_name = forms.CharField(max_length=50, label="Sobrenome")
    email = forms.EmailField(label="Seu Email")
    message = forms.CharField(widget=forms.Textarea, label="Mensagem")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona as classes de estilo a todos os campos
        self.fields['first_name'].widget.attrs.update({'class': 'w-full bg-gray-700 text-white border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400', 'placeholder': 'Jean'})
        self.fields['last_name'].widget.attrs.update({'class': 'w-full bg-gray-700 text-white border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400', 'placeholder': 'Rufino'})
        self.fields['email'].widget.attrs.update({'class': 'w-full bg-gray-700 text-white border-gray-600 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400', 'placeholder': 'seu@email.com'})
        self.fields['message'].widget.attrs.update({'class': 'w-full bg-gray-700 text-white border-gray-600 rounded-lg p-3 h-32 focus:outline-none focus:ring-2 focus:ring-cyan-400', 'placeholder': 'Olá, gostaria de falar sobre...'})