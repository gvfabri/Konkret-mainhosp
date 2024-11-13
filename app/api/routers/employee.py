from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Annotated
from app.api.services.employee_service import EmployeeService
from app.api.dependencies import get_employee_service

router = APIRouter(
    prefix="/employee",
    tags=["employee"]
)

@router.post("")
def add_employee(
    name: Annotated[str, Query()],
    rg: Annotated[int, Query()],
    cpf: Annotated[int, Query()],
    role: Annotated[str, Query()],
    salary: Annotated[float, Query()],
    work_id: Annotated[str, Query()],
    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]
):    
    try:
        return employee_service.create_employee(name, rg, cpf, role, salary, work_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.put("/{id}/update")
def update_employee(
    id: str,
    salary: Annotated[float, Query()],
    role: Annotated[str, Query()],
    work_id: Annotated[str, Query()],
    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]
):
    try: 
        updated_employee = employee_service.update(id, salary, role, work_id)
        if isinstance(updated_employee, str):
            raise HTTPException(status_code=404)
        return updated_employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.get("")
def getall_employees(
    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]
):
    try:
        return employee_service.all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}")
def get_employee(
    id: str,
    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]
):
    try:
        employee = employee_service.get(id)
        if employee is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
        return employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.delete("/{id}")
def delete_employee(
    id:str,
    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]
):
    try:
        result = employee_service.delete(id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")