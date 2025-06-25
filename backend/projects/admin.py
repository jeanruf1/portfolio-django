# backend/projects/admin.py

from django.contrib import admin
from .models import Project # Importa o seu modelo "Project"

# A anotação @admin.register é a forma moderna e recomendada de registrar um modelo
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Campos que aparecerão na lista de projetos para fácil visualização
    list_display = ('title', 'is_published', 'created_at')
    
    # Adiciona uma barra lateral com filtros
    list_filter = ('is_published',)
    
    # Adiciona um campo de busca que procura no título e na descrição
    search_fields = ('title', 'description')
    
    # Um truque muito útil: preenche o campo 'slug' automaticamente
    # com base no que você digita no 'title'.
    prepopulated_fields = {'slug': ('title',)}