from ..repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

class UserService:
    def __init__(self, db: Session):
        self.buyer_repository = UserRepository(db)

    def create_user(self,name: str,phone: str,email: str):
        self.buyer_repository.create(name,phone,email)

    