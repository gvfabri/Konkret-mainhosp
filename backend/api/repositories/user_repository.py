from backend.api.core.models import User, Work
from sqlalchemy.orm import Session
import bcrypt
from passlib.context import CryptContext
import re
from backend.api.utils import pwd_context

class UserRepository:
    def __init__(self,db: Session):
        self.db = db

    def create(self,name: str,cpf: str,email: str, password: str):
        cpf = re.sub(r'[^0-9]', '', cpf)
        hashed_password = pwd_context.hash(password)
        new_user = User(name=name,cpf=cpf,email=email, password=hashed_password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user 
    
    def update(self, id: str, cpf: str = None, email: str = None,  password: str = None):
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            if cpf is not None:
                user.cpf = cpf
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
            return user
        return None
    
    def find_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()