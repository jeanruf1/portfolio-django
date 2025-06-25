# backend/projects/models.py
from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, blank=True, help_text="Gerado automaticamente, não preencher.")
    cover = models.ImageField(upload_to='project_covers/', verbose_name="Capa do Projeto")
    description = models.TextField(verbose_name="Descrição")
    video_url = models.URLField(blank=True, null=True, verbose_name="URL do Vídeo")
    video_file = models.FileField(upload_to='project_videos/', blank=True, null=True, verbose_name="Ou Envie um Vídeo (MP4)")
    tech_details = models.TextField(verbose_name="Detalhes Técnicos")
    github_url = models.URLField(blank=True, null=True, verbose_name="URL do Repositório no GitHub")
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="Publicado")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-created_at']