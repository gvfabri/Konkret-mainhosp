from ..core.models import MaoDeObra
from sqlalchemy.orm import Session

class MaoDeObraRepository:
    def __init__(self,db: Session):
        self.db = db

    def create_mao_de_obra(self,nome: str, rg: str,cpf: str, cargo: str, salario: str):
        new_mao_de_obra = MaoDeObra(nome,rg, cpf, cargo, salario)
        self.db.add(new_mao_de_obra)
        self.db.commit()
        self.db.refresh(new_mao_de_obra)
        return new_mao_de_obra
    
    #Colocando float = None e str = None, faz com que de pra atualizar só um dos dados
    def update(self, id_funcionario: str, salario: float = None, cargo: str = None):
        mao_de_obra = self.db.query(MaoDeObra).filter(MaoDeObra.id_funcionario == id_funcionario).first()
        if mao_de_obra:
            if salario is not None:
                mao_de_obra.salario = salario
            if cargo is not None:
                mao_de_obra.cargo = cargo
            self.db.commit()
            self.db.refresh(mao_de_obra)
            return "Dados atusalizados com sucesso!", mao_de_obra
        return f"{id_funcionario} não encontrado!"
    
    #Usar firts() ao inves de one(), pois first considera que só terá um item a ser encontrado, como o id é único
    def delete(self, id_funcionario: str):
        mao_de_obra = self.db.query(MaoDeObra).filter(MaoDeObra.id_funcionario == id_funcionario).first()
        if mao_de_obra:
            self.db.delete(mao_de_obra)
            self.db.commit()
            return f"Funcionário {id_funcionario} deletado."
        return f"{id_funcionario} não encontrado!"
    