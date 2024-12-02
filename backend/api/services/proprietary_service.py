from backend.api.repositories.proprietary_repository import ProprietaryRepository
from sqlalchemy.orm import Session

class ProprietaryService:
    def __init__(self, db: Session):
        self.proprietary_repository = ProprietaryRepository(db)

    def create_proprietary(self, name: str, cpf: str):
        return self.proprietary_repository.create_proprietary(name, cpf)

    def all(self):
        return self.proprietary_repository.all()

    def get(self, id: str):
        return self.proprietary_repository.get(id)
 
    def delete(self, id: str):
        return self.proprietary_repository.delete(id)
    
    def works(self, id: str):
        return self.proprietary_repository.works(id)
        