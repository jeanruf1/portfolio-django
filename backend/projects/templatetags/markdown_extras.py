# backend/projects/templatetags/markdown_extras.py

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown2

register = template.Library()

# Filtro para converter a URL do YouTube
@register.filter(name='youtube_embed_url')
@stringfilter
def youtube_embed_url(value):
    if "watch?v=" in value:
        video_id = value.split('watch?v=')[1]
        if '&' in video_id:
            video_id = video_id.split('&')[0]
        return f"https://www.youtube.com/embed/{video_id}"
    return value

# Filtro para renderizar Markdown
@register.filter(name='markdownify')
@stringfilter
def markdownify(value):
    html = markdown2.markdown(value, extras=['fenced-code-blocks', 'cuddled-lists'])
    return mark_safe(html)

# --- NOVOS FILTROS ADICIONADOS ---

# Filtro para dividir uma string por um delimitador
@register.filter(name='split')
@stringfilter
def split_string(value, key=','):
    return value.split(key)

# Filtro para remover espaços em branco do início e do fim
@register.filter(name='trim')
@stringfilter
def trim_string(value):
    return value.strip()