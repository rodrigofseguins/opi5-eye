
# Projeto opi5-eye

## Descrição

O projeto "opi5-eye" é uma ferramenta desenvolvida em Python para monitorar, verificar, comitar e enviar alterações em pastas de containers Docker para repositórios Git. A ferramenta é projetada para ser usada em linha de comando e pode ser executada automaticamente através de cron jobs. A implementação e a configuração são feitas para rodar em um ambiente Linux, mais especificamente em um dispositivo Orange Pi 5, utilizando Docker e Ansible para gerenciar a infraestrutura.

## Estrutura do Projeto

```plaintext
opi5-eye/
│
├── Dockerfile
├── docker-compose.yml
├── inventory
│   ├── hosts.yml
├── playbook.yml
├── vars.yml
├── templates/
│   ├── env.j2
├── load_config.py
├── commit_and_push.py
├── requirements.txt
└── venv/
```

## Componentes Principais

1. **Dockerfile**: Define o ambiente Docker necessário para o projeto, incluindo todas as dependências.
2. **docker-compose.yml**: Configura como os serviços Docker serão montados e conectados.
3. **inventory**: Diretório contendo o arquivo `hosts.yml` usado pelo Ansible para definir os hosts e grupos de hosts a serem gerenciados.
4. **playbook.yml**: Playbook Ansible que define as tarefas a serem executadas no host, incluindo a configuração do ambiente e a execução de scripts.
5. **vars.yml**: Arquivo contendo variáveis usadas no playbook Ansible.
6. **templates**: Diretório contendo templates Jinja2, como `env.j2`, usado para gerar arquivos de configuração dinâmicos.
7. **load_config.py**: Script Python que carrega as configurações a partir de um arquivo `.env`.
8. **commit_and_push.py**: Script Python que verifica alterações nas pastas dos containers, comita essas alterações e as envia para os repositórios Git correspondentes.
9. **requirements.txt**: Arquivo que lista as dependências Python do projeto.
10. **venv**: Diretório onde é criado o ambiente virtual Python para desenvolvimento.

## Funcionalidades

1. **Monitoramento e Verificação**: O script `commit_and_push.py` verifica alterações nas pastas dos containers especificadas em `CONTAINER_PATHS`.
2. **Commit e Push Automático**: O script comita e envia automaticamente as alterações para os repositórios Git configurados.
3. **Configuração Flexível**: Carrega configurações de um arquivo `.env`, permitindo ajustes fáceis de variáveis de ambiente e parâmetros do projeto.
4. **Execução Automatizada**: Projetado para ser executado como um cron job, permitindo verificações periódicas e automáticas.
5. **Gerenciamento com Ansible**: O Ansible é usado para configurar o ambiente e gerenciar a execução dos scripts no host.

## Configuração e Uso

1. **Configuração do Arquivo `.env`**:
   - Crie um arquivo chamado `.env` na raiz do projeto com as seguintes variáveis:
     ```env
     GIT_REPOS=git@github.com:usuario/repo1.git,git@github.com:usuario/repo2.git,git@github.com:usuario/repo3.git
     GIT_BRANCHES=main,main,main
     CONTAINER_PATHS=/root/containers/container1,/root/containers/container2,/root/containers/container3
     ```

2. **Criação do Ambiente Virtual**:
   - No ambiente de desenvolvimento, crie um ambiente virtual Python:
     - Execute `python -m venv venv` para criar o ambiente virtual.
     - Ative o ambiente virtual com `source venv/bin/activate`.
     - Instale as dependências listadas no arquivo `requirements.txt` usando `pip install -r requirements.txt`.

3. **Build e Deploy com Docker**:
   - Para construir e executar o container Docker, use o comando:
     - `docker-compose up --build -d`.

4. **Execução com Ansible**:
   - Use o Ansible para configurar o ambiente e executar os scripts:
     - Execute o playbook Ansible com `ansible-playbook -i inventory/hosts.yml playbook.yml`.

## Exemplo de Uso com Cron Job

Para automatizar a execução do script de commit e push, adicione uma entrada no cron para executar periodicamente. Por exemplo, para executar a cada hora:

- Adicione a linha `0 * * * * cd /caminho/para/opi5-eye && ./venv/bin/python commit_and_push.py` no arquivo de crontab (`crontab -e`).

## Gerenciamento de Chaves SSH

### Gerar uma Nova Chave SSH

Caso você ainda não tenha uma chave SSH configurada, siga os passos abaixo para gerar uma:

1. **Gerar a chave SSH**:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "seu_email@example.com"
   ```
   Pressione Enter para aceitar o local padrão do arquivo.

2. **Adicionar a chave SSH ao ssh-agent**:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_rsa
   ```

3. **Copiar a chave SSH para o servidor remoto**:
   ```bash
   ssh-copy-id -i ~/.ssh/id_rsa.pub usuario@192.168.100.40
   ```

### Adicionar a Chave SSH ao GitHub/GitLab

Para adicionar a chave SSH ao GitHub ou GitLab:

1. **Copiar o conteúdo da chave pública**:
   ```bash
   cat ~/.ssh/id_rsa.pub
   ```

2. **Adicionar a chave ao GitHub/GitLab**:
   - No GitHub, vá para **Settings** > **SSH and GPG keys** > **New SSH key** e cole a chave pública.
   - No GitLab, vá para **Settings** > **SSH Keys** > **Add SSH Key** e cole a chave pública.

## Considerações Finais

O projeto "opi5-eye" oferece uma solução robusta e automatizada para monitorar e gerenciar alterações em pastas de containers Docker. Ele garante que todas as mudanças sejam comitadas e enviadas para os repositórios Git de maneira eficiente e confiável, facilitando a gestão de configurações e a automação de processos em um ambiente de desenvolvimento contínuo.
