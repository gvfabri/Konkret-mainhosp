from app.api.repositories.employee_repository import EmployeeRepository
from sqlalchemy.orm import Session

class EmployeeService:
    def __init__(self, db: Session):
        self.employee_repository = EmployeeRepository(db)

    def create_employee(self, name: str, rg: int, cpf: int, role: str, salary: float, work_id: str):
        self.employee_repository.create_employee(name,rg,cpf,role,salary,work_id)

    def all(self):
        return self.employee_repository.all()

    def get(self, id: str):
        return self.employee_repository.get(id)
    
    def update(self, id: str, salary: float = None, role: str = None, work_id: str = None):
        self.employee_repository.update(id, salary, role)
    
    def delete(self, id: str):
        self.employee_repository.delete(id)
        