from fastapi import APIRouter, Request, Query, Depends, HTTPException
from typing import Annotated
import json
from ...services.user_service import UserService
from ...services.work_service import WorkService
from ...services.employee_service import EmployeeService
from ...services.proprietary_service import ProprietaryService
from ...dependencies import get_user_service, get_employee_service, get_work_service, get_proprietary_service

router = APIRouter()

@router.post("/user")
def add_user(
    name: Annotated[str, Query()],
    phone: Annotated[str, Query()],
    email: Annotated[str, Query()],
    password: Annotated[str, Query()],
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        user = user_service.create_user(name,phone,email, password)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")

@router.put("/user/{id}/update")
def update_user(
    id: str,
    phone: Annotated[str, Query()],
    email: Annotated[str, Query()],
    password: Annotated[str, Query()],
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try: 
        updated_user = user_service.update(id, phone, email, password)
        if isinstance(updated_user, str):
            raise HTTPException(status_code=404)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")

@router.get("/user")
def getall_users(
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        return user_service.all()
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.get("/user/{id}")
def get_user(
    id: str,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        return user_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.delete("/user/{id}")
def delete_user(
    id: str,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        user_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.post("/employee")
def add_employee(
    name: Annotated[str, Query()],
    rg: Annotated[int, Query()],
    cpf: Annotated[int, Query()],
    role: Annotated[str, Query()],
    salary: Annotated[float, Query()],
    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]
):    
    try:
        employee_service.create_employee(name, rg, cpf, role, salary)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.put("/employee/{id}/update")
def update_employee(
    id: str,
    salary: Annotated[float, Query()],
    role: Annotated[str, Query()],
    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]
):
    try: 
        updated_employee = employee_service.update(id, salary, role)
        if isinstance(updated_employee, str):
            raise HTTPException(status_code=404)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.get("/employee")
def getall_employees(
    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]
):
    try:
        return employee_service.all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.get("/employee/{id}")
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
    
@router.delete("/employee/{id}")
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
    

@router.post("/work")
def add_work(
    address: Annotated[str, Query()],
    photos: Annotated[list, Query()],
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        work_service.create_work(address, photos)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.put("/work/{id}/addphoto")
def add_photo(
    id: str,
    photo: Annotated[str, Query()],
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        work_service.add_photo(id, photo)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.put("/work/{id}/removephoto")
def remove_photo(
    id: str,
    photo: Annotated[str, Query()],
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        work_service.remove_photo(id, photo)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.get("/work")
def getall_works(
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.all()
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.get("/work/{id}")
def get_work(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.delete("/work/{id}")
def delete_work(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        work_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    

@router.post("/proprietary")
def add_proprietary(
    name: Annotated[str, Query()],
    cpf: Annotated[str, Query()],
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        proprietary = proprietary_service.create_proprietary(name,cpf)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")

@router.get("/proprietary")
def getall_proprietaries(
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        return proprietary_service.all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.get("/proprietary/{id}")
def get_proprietary(
    proprietary_service: Annotated[EmployeeService, Depends(get_proprietary_service)]
):
    try:
        proprietary = proprietary_service.get(id)
        if proprietary is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
        return proprietary
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.delete("/proprietary/{id}")
def delete_proprietary(
    id:str,
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        result = proprietary_service.delete(id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
