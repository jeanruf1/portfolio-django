# backend/portfolio_project/urls.py <--- ESTE É O RECEPCIONISTA

from django.contrib import admin
from django.urls import path, include # Importando a função 'include'
from django.conf import settings
from django.conf.urls.static import static
from projects.views import HomeView, AboutView, ContactView

# A única função do recepcionista é direcionar para os departamentos
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('sobre/', AboutView.as_view(), name='about'),
    path('contato/', ContactView.as_view(), name='contact'), # <-- NOVA ROTA AQUI
    path('projetos/', include('projects.urls', namespace='projects')),
]

# Lógica para servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)