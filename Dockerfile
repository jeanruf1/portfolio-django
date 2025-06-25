# Dockerfile

# 1. Imagem base do Python
FROM python:3.11-slim

# 2. Instala o Node.js e o npm
RUN apt-get update && apt-get install -y nodejs npm
RUN rm -rf /var/lib/apt/lists/*

# 3. Define variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# 5. Instala as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia o código do seu backend para dentro do contêiner
COPY ./backend /app

# 7. Instala as dependências do Node.js
# VAI PARA A PASTA CORRETA ONDE O package.json REALMENTE ESTÁ!
WORKDIR /app/theme/static_src
RUN npm install

# Retorna ao diretório de trabalho principal da aplicação
WORKDIR /app