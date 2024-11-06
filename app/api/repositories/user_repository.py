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
    
    def update(self, id: str, phone: str = None, email: str = None):
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            if phone is not None:
                user.phone = phone
            if email is not None:
                user.email = email
            self.db.commit()
            self.db.refresh(email)
            return user
        return False
    
    def all(self):
        return self.db.query(User).all()
    
    def get(self, id: str):
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            return user
        return False
    
    def delete(self, id: str):
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False