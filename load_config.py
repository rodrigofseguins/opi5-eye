import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
git_repos = os.getenv('GIT_REPOS').split(',')
git_branches = os.getenv('GIT_BRANCHES').split(',')
container_paths = os.getenv('CONTAINER_PATHS').split(',')

# Exibir as variáveis para verificar se foram carregadas corretamente
print(f'GIT_REPOS: {git_repos}')
print(f'GIT_BRANCHES: {git_branches}')
print(f'CONTAINER_PATHS: {container_paths}')
