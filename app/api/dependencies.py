from .services.user_service import UserService
from .core.session import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated

def get_user_service(db: Annotated[Session, Depends(get_db)]):
    return UserService(db)