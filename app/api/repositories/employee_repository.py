from ..core.models import Employee
from sqlalchemy.orm import Session

class EmployeeRepository:
    def __init__(self,db: Session):
        self.db = db

    def create_employee(self,name: str, rg: int,cpf: int, role: str, salary: float):
        new_employee = Employee(name=name,rg=rg, cpf=cpf, role=role, salary=salary)
        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        return new_employee
    
    #Colocando float = None e str = None, faz com que de pra atualizar só um dos dados
    def update(self, id: str, salary: float = None, role: str = None):
        employee = self.db.query(Employee).filter(Employee.id == id).first()
        if employee:
            if salary is not None:
                employee.salary = salary
            if role is not None:
                employee.role = role
            self.db.commit()
            self.db.refresh(employee)
            return employee
        return False
    
    def all(self):
        return self.db.query(Employee).all()
    
    def get(self, id: str):
        employee = self.db.query(Employee).filter(Employee.id == id).first()
        if employee:
            return employee
        return False
    
    #Usar firts() ao inves de one(), pois first considera que só terá um item a ser encontrado, como o id é único
    def delete(self, id: str):
        employee = self.db.query(Employee).filter(Employee.id == id).first()
        if employee:
            self.db.delete(employee)
            self.db.commit()
            return True
        return False
    