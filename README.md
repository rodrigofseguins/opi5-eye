
# Projeto opi5-eye

## Descrição

O projeto "opi5-eye" é uma ferramenta desenvolvida em Python para monitorar, verificar, comitar e enviar alterações em pastas de containers Docker para um repositório Git. A ferramenta é projetada para ser usada em linha de comando e pode ser executada automaticamente através de cron jobs. A implementação e a configuração são feitas para rodar em um ambiente Linux, mais especificamente em um dispositivo Orange Pi 5, utilizando Docker e Ansible para gerenciar a infraestrutura.

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
8. **commit_and_push.py**: Script Python que verifica alterações nas pastas dos containers, comita essas alterações e as envia para o repositório Git.
9. **requirements.txt**: Arquivo que lista as dependências Python do projeto.
10. **venv**: Diretório onde é criado o ambiente virtual Python para desenvolvimento.

## Funcionalidades

1. **Monitoramento e Verificação**: O script `commit_and_push.py` verifica alterações nas pastas dos containers especificadas em `CONTAINER_PATHS`.
2. **Commit e Push Automático**: O script comita e envia automaticamente as alterações para o repositório Git configurado.
3. **Configuração Flexível**: Carrega configurações de um arquivo `.env`, permitindo ajustes fáceis de variáveis de ambiente e parâmetros do projeto.
4. **Execução Automatizada**: Projetado para ser executado como um cron job, permitindo verificações periódicas e automáticas.
5. **Gerenciamento com Ansible**: O Ansible é usado para configurar o ambiente e gerenciar a execução dos scripts no host.

## Configuração e Uso

1. **Configuração do Arquivo `.env`**:
   - Crie um arquivo chamado `.env` na raiz do projeto com as seguintes variáveis:
     ```env
     GIT_REPO_URL=git@github.com:usuario/repositorio.git
     GIT_BRANCH=main
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

## Considerações Finais

O projeto "opi5-eye" oferece uma solução robusta e automatizada para monitorar e gerenciar alterações em pastas de containers Docker. Ele garante que todas as mudanças sejam comitadas e enviadas para um repositório Git de maneira eficiente e confiável, facilitando a gestão de configurações e a automação de processos em um ambiente de desenvolvimento contínuo.
