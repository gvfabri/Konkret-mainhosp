from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from pydantic import BaseModel
from backend.api.core.models import Base
import psycopg2

# Get the database credentials from environment variables
host = os.environ.get('DB_HOST')
database = os.environ.get('DB_NAME')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')

# Define the connection string
connection_string = f"host={host} dbname={database} user={user} password={password}"

# Connect to the database
connection = psycopg2.connect(connection_string)

# Pega a URL do banco de dados do arquivo .env
#DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql://postgres:postgres@localhost:5434/postgres_db"

# Configurando o engine com parâmetros otimizados para evitar erros de conexão
engine = create_engine(
    DATABASE_URL,
    pool_size=10, # Tamanho inicial do pool de conexões
    max_overflow=20, # Conexões extras permitidas em casos de alta carga
    pool_timeout=30, # Tempo máximo de espera para uma conexão disponível
    pool_recycle=1800, # Tempo para reciclar conexões (em segundos)
    pool_pre_ping=True, # Verifica a saúde da conexão antes de utilizá-la
)

# Criando uma sessão com as configurações otimizadas
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependência para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Cria as tabelas no banco de dados, se ainda não existirem
#Base.metadata.drop_all(bind=engine)  # Apaga todas as tabelas
Base.metadata.create_all(bind=engine)  # Recria as tabelas
