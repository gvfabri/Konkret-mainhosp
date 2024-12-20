# Escolher a imagem base do Python
FROM python:3.11-slim

# Instalar dependências do sistema necessárias (curl e qualquer outro pacote necessário)
RUN apt-get update && apt-get install -y curl

# Instalar o gerenciador de pacotes 'uv' diretamente com o Python (caso o comando 'curl' falhe)
RUN pip install uv

# Definir o diretório de trabalho
WORKDIR /app

# Copiar todos os arquivos do repositório para o diretório de trabalho no container
COPY . /app

# Sincronizar as dependências com o 'uv'
RUN uv sync

# Expor a porta que o FastAPI irá rodar
EXPOSE 8000

# Comando para rodar a aplicação (substitua o caminho para o arquivo main correto, caso necessário)
CMD ["uv", "run", "uvicorn", "backend.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
