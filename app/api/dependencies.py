from .services.user_service import UserService
from .services.employee_service import EmployeeService
from .services.work_service import WorkService
from .services.proprietary_service import ProprietaryService
from .core.session import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated

def get_user_service(db: Annotated[Session, Depends(get_db)]):
    return UserService(db)

def get_employee_service(db: Annotated[Session, Depends(get_db)]):
    return EmployeeService(db)

def get_work_service(db: Annotated[Session, Depends(get_db)]):
    return WorkService(db)
def get_proprietary_service(db: Annotated[Session, Depends(get_db)]):
    return ProprietaryService(db)