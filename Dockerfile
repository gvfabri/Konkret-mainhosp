# Etapa 1: Base do Python
FROM python:3.11-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o uv para gerenciar a execução
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Expor a porta da API
EXPOSE 8000


# Comando para rodar a API com o Uvicorn
CMD ["sh", "-c", "uv run alembic upgrade head && uv run uvicorn backend.api.main:app --host 0.0.0.0 --reload"]
