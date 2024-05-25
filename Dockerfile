# Usar uma imagem base oficial do Python
FROM python:3.10-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    sshpass \
    git \
    && apt-get clean

# Instalar Ansible
RUN pip install ansible

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo requirements.txt e o restante do conteúdo do diretório local para o diretório de trabalho no container
COPY requirements.txt ./
COPY . .

# Instalar as dependências do projeto
RUN pip install -r requirements.txt

# Comando para manter o container em execução
CMD ["tail", "-f", "/dev/null"]
