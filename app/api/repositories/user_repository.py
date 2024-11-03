from ..core.models import User
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self,db: Session):
        self.db = db

    def create(self,name: str,phone: str,email: str):
        new_user = User(name=name,phone=phone,email=email)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user 