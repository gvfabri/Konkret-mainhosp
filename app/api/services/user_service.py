from ..repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self,name: str,phone: str,email: str, password: str):
        self.user_repository.create(name,phone,email, password)

    def update(self, id: str, phone: str = None, email: str = None, password: str = None):
        self.user_repository.update(id, phone, email, password)

    def all(self):
        return self.user_repository.all()

    def get(self, id: str):
        return self.user_repository.get(id)
    
    def delete(self, id: str):
        self.user_repository.delete(id)