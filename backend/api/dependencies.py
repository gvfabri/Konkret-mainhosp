from backend.api.services.user_service import UserService
from backend.api.services.employee_service import EmployeeService
from backend.api.services.report_service import ReportService
from backend.api.services.proprietary_service import ProprietaryService
from backend.api.services.work_service import WorkService
from backend.api.core.session import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated

def get_user_service(db: Annotated[Session, Depends(get_db)]):
    return UserService(db)

def get_employee_service(db: Annotated[Session, Depends(get_db)]):
    return EmployeeService(db)

def get_report_service(db: Annotated[Session, Depends(get_db)]):
    return ReportService(db)

def get_proprietary_service(db: Annotated[Session, Depends(get_db)]):
    return ProprietaryService(db)

def get_work_service(db: Annotated[Session, Depends(get_db)]):
    return WorkService(db)