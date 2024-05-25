import os
import subprocess
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
git_repos = os.getenv('GIT_REPOS').split(',')
git_branches = os.getenv('GIT_BRANCHES').split(',')
container_paths = os.getenv('CONTAINER_PATHS').split(',')

# Função para executar comandos no shell
def run_shell_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erro ao executar comando: {result.stderr}")
    return result.stdout

# Processar cada container path
for repo, branch, container_path in zip(git_repos, git_branches, container_paths):
    print(f"Processando: {container_path}")

    # Verificar status do git
    run_shell_command(f"cd {container_path} && git status")

    # Adicionar mudanças ao staging
    run_shell_command(f"cd {container_path} && git add .")

    # Comitar mudanças
    commit_message = f"Automated commit for {container_path}"
    run_shell_command(f'cd {container_path} && git commit -m "{commit_message}"')

    # Enviar para o repositório remoto
    run_shell_command(f"cd {container_path} && git push {repo} {branch}")

print("Mudanças comitadas e enviadas com sucesso!")
