from ..core.models import Proprietary, Work
from sqlalchemy.orm import Session

class ProprietaryRepository:
    def __init__(self,db: Session):
        self.db = db

    def create_proprietary(self,name: str,cpf: str):
        new_proprietary = Proprietary(name=name, cpf=cpf)
        self.db.add(new_proprietary)
        self.db.commit()
        self.db.refresh(new_proprietary)
        return new_proprietary
    
    def all(self):
        return self.db.query(Proprietary).all()
    
    def get(self, id: str):
        proprietary = self.db.query(Proprietary).filter(Proprietary.id == id).first()
        if proprietary:
            return proprietary
        return False
    
    #Usar firts() ao inves de one(), pois first considera que só terá um item a ser encontrado, como o id é único
    def delete(self, id: str):
        proprietary = self.db.query(Proprietary).filter(Proprietary.id == id).first()
        works = self.db.query(Work).all()
        if proprietary:
            for work in works:
                if proprietary.id in work.proprietaries:
                    Work.proprietaries.remove(proprietary.id)
            self.db.delete(proprietary)
            self.db.commit()
            return True
        return False