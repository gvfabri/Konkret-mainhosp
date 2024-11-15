from backend.api.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self,name: str,cpf: str,email: str, password: str):
        self.user_repository.create(name,cpf,email, password)

    def update(self, id: str, cpf: str = None, email: str = None, password: str = None):
        self.user_repository.update(id, cpf, email, password)

    def all(self):
        return self.user_repository.all()

    def get(self, id: str):
        return self.user_repository.get(id)
    
    def delete(self, id: str):
        self.user_repository.delete(id)