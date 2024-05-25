# Projeto opi5-eye

## Descrição

O projeto "opi5-eye" é uma ferramenta Python desenvolvida para monitorar, verificar, comitar e enviar alterações em pastas de containers Docker para um repositório Git. A ferramenta é projetada para ser usada em linha de comando e pode ser executada automaticamente via cron jobs. A implementação e a configuração são feitas para rodar em um ambiente Linux, mais especificamente em um Orange Pi 5, usando Docker e Ansible para gerenciar a infraestrutura.

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


## Componentes Principais