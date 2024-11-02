from ..repositories.mao_de_obra_repository import MaoDeObraRepository
from sqlalchemy.orm import Session

class MaoDeObraService:
    def __init__(self, db: Session):
        self.mao_de_obra_repository = MaoDeObraRepository(db)

    def create_mao_de_obra(self,nome: str, rg: str, cpf: str, cargo: str, salario: float):
        self.mao_de_obra_repository.create_mao_de_obra(nome,rg,cpf,cargo,salario)
    
    def uptade(self, id_funcionario: str, salario: float = None, cargo: str = None):
        self.mao_de_obra_repository.update(id_funcionario, salario, cargo)
    
    def delete(self, id_funcionario: str):
        self.mao_de_obra_repository.delete(id_funcionario)
        