# Use uma imagem base oficial do Python
FROM python:3.12-slim

# Instale o curl e dependências necessárias para psycopg2
RUN apt-get update && apt-get install -y curl gcc libpq-dev

# Instale o uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Defina o PATH para incluir o diretório onde o uv foi instalado
ENV PATH="/root/.local/bin:${PATH}"

# Crie um diretório de trabalho
WORKDIR /app

# Copie todos os arquivos do app para o diretório de trabalho
COPY . .

# Instale as dependências usando uv sync e depois instale psycopg2
RUN uv sync --frozen --no-cache && pip install psycopg2-binary

# Exponha a porta em que a aplicação será executada
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "backend.api.main:app", "--port", "8000", "--host", "0.0.0.0"]
