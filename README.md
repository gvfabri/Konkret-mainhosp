# Konkret

Konkret é um aplicativo que serve como um diário de pedreiro, auxiliando o eng. civil no seu trabalho cotidiano.

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/ES2024Konkret/Konkret-main
```

## Pré requisitos

1. **Instale o gerenciador de pacotes uv**: 
rode as seguintes linhas no terminal
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Ativação

1. Dê up no container
```bash
docker compose up --build
```

2. atualize as dependencies
```bash
uv sync
```

3. Atualize as bases de dados
```bash
uv run alembic upgrade head
```

## Uso

Após a execução do container, acesse o postgres com o seguinte comando
```bash
docker exec -it konkret-main-db-1 psql -U postgres -d postgres_db
```

Então use o uvicorn para rodar um server local
```bash
uv run uvicorn backend.api.main:app
```

Para abrir a página, primeiro entre na pasta do Frontend
```bash
cd frontend/
```

Instale npm
```bash
cd npm i
```

Inicie o Frontend
```bash
npm run dev
```
