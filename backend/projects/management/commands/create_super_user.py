# backend/projects/management/commands/create_super_user.py

import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Cria um superusuário automaticamente a partir de variáveis de ambiente.'

    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USER')
        email = os.environ.get('ADMIN_EMAIL')
        password = os.environ.get('ADMIN_PASSWORD')

        if not all([username, email, password]):
            self.stdout.write(self.style.ERROR('As variáveis de ambiente ADMIN_USER, ADMIN_EMAIL e ADMIN_PASSWORD devem ser definidas.'))
            return

        if not User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f'Criando superusuário: {username}'))
            User.objects.create_superuser(username=username, email=email, password=password)
        else:
            self.stdout.write(self.style.WARNING(f'Superusuário "{username}" já existe.'))