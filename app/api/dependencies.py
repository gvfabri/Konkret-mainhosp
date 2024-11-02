from .services.user_service import UserService
from .services.mao_de_obra_service import MaoDeObraService
from .core.session import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated

def get_user_service(db: Annotated[Session, Depends(get_db)]):
    return UserService(db)

def get_mao_de_obra_service(db: Annotated[Session, Depends(get_db)]):
    return MaoDeObraService(db)