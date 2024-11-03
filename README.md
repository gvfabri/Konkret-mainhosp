# Konkret

Konkret é um aplicativo que serve como um diário de pedreiro, auxiliando o eng. civil
no seu trabalho cotidiano.

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/ES2024Konkret/Konkret-main
```

2. Crie um ambient
```bash
python -m venv env
```

3. Ative o ambiente
```bash
source env/bin/activate
```

4. Instale os requerimentos
```bash
pip install -r requirements.txt
```

5. Execute o container
```bash
docker compose up
```

6. Execute o alembic
```bash
alembic upgrade head
```

## Uso

Após a execução do container, acesse o postgres com o seguinte comando
```bash
docker exec -it konkret-main-db-1 psql -U postgres -d postgres_db
```
