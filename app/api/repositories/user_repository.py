from app.api.core.models import User, Work
from sqlalchemy.orm import Session
import bcrypt

class UserRepository:
    def __init__(self,db: Session):
        self.db = db

    def create(self,name: str,phone: str,email: str, password: str):
        new_user = User(name=name,phone=phone,email=email, password=password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user 
    
    def update(self, id: str, phone: str = None, email: str = None,  password: str = None):
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            if phone is not None:
                user.phone = phone
            if email is not None:
                user.email = email
            if password is not None:
            # Gera um hash para o password
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                user.password = hashed_password
            self.db.commit()
            self.db.refresh(user)
            return user
        return None
    
    def all(self):
        return self.db.query(User).all()
    
    def get(self, id: str):
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            return user
        return None
    
    def delete(self, id: str):
        user = self.db.query(User).filter(User.id == id).first()
        works = self.db.query(Work).all()
        if user:
            for work in works:
                if user.id in work.workers:
                    Work.workers.remove(user.id)
            self.db.delete(user)
            self.db.commit()
            return True
        return None