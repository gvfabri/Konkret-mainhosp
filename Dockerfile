# Use uma imagem base oficial do Python
FROM python:3.10

# Crie um diretório de trabalho
WORKDIR /app

# Instale o uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copie todos os arquivos do app para o diretório de trabalho
COPY . .

# Exponha a porta em que a aplicação será executada
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["sh", "-c", "uv sync && uv run alembic upgrade head && uv run uvicorn backend.api.main:app --host 0.0.0.0 --reload"]
