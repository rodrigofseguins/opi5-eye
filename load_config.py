import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
git_repo_url = os.getenv('GIT_REPO_URL')
git_branch = os.getenv('GIT_BRANCH')
container_paths = os.getenv('CONTAINER_PATHS').split(',')

# Exibir as variáveis para verificar se foram carregadas corretamente
print(f'GIT_REPO_URL: {git_repo_url}')
print(f'GIT_BRANCH: {git_branch}')
print(f'CONTAINER_PATHS: {container_paths}')
