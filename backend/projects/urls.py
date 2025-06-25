# backend/projects/urls.py
from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='list'),
    path('criar/', ProjectCreateView.as_view(), name='create'),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='detail'),
    path('<slug:slug>/editar/', ProjectUpdateView.as_view(), name='update'),
    # NOVA ROTA PARA EXCLUSÃO
    path('<slug:slug>/excluir/', ProjectDeleteView.as_view(), name='delete'),
]