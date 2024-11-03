from fastapi import APIRouter, Request, Query, Depends, HTTPException
from typing import Annotated
import json
from ...services.user_service import UserService
from ...services.workframe_service import WorkframeService
from ...services.mao_de_obra_service import MaoDeObraService
from ...dependencies import get_user_service, get_mao_de_obra_service, get_workframe_service

router = APIRouter()

@router.post("/add-user")
def add_user(
    name: Annotated[str, Query()],
    user_phone: Annotated[str, Query()],
    user_email: Annotated[str, Query()],
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        user = user_service.create_user(name,user_phone,user_email)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")

#post cria, put atualiza e delete deleta
@router.post("/add-mao-de-obra")
def add_mao_de_obra(
    nome: Annotated[str, Query()],
    mao_de_obra_rg: Annotated[str, Query()],
    mao_de_obra_cpf: Annotated[str, Query()],
    mao_de_obra_cargo: Annotated[str, Query()],
    mao_de_obra_salario: Annotated[float, Query()],
    mao_de_obra_service: Annotated[MaoDeObraService, Depends(get_mao_de_obra_service)]
):    
    try:
        add_mao_de_obra = mao_de_obra_service.create_mao_de_obra(
            nome, mao_de_obra_rg, mao_de_obra_cpf, mao_de_obra_cargo, mao_de_obra_salario)
        if isinstance(add_mao_de_obra, str):
            raise HTTPException(status_code=404, detail=add_mao_de_obra)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")

@router.post("/workframe")
def add_workframe(
    address: Annotated[str, Query()],
    photos: Annotated[list, Query()],
    workframe_service: Annotated[WorkframeService, Depends(get_workframe_service)]
):
    try:
        user = workframe_service.create_workframe(address, photos)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.put("/workframe/{id}/addphoto")
def add_photo_to_workframe(
    id: str,
    photo: Annotated[str, Query()],
    workframe_service: Annotated[WorkframeService, Depends(get_workframe_service)]
):
    try:
        workframe_service.add_photo(id, photo)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.put("/workframe/{id}/removephoto")
def remove_photo_from_workframe(
    id: str,
    photo: Annotated[str, Query()],
    workframe_service: Annotated[WorkframeService, Depends(get_workframe_service)]
):
    try:
        workframe_service.remove_photo(id, photo)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.get("/workframe")
def get_workframes(
    workframe_service: Annotated[WorkframeService, Depends(get_workframe_service)]
):
    try:
        return workframe_service.all()
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.get("/workframe/{id}")
def get_workframe(
    id: str,
    workframe_service: Annotated[WorkframeService, Depends(get_workframe_service)]
):
    try:
        return workframe_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")
    
@router.delete("/workframe/{id}")
def delete_workframe(
    id: str,
    workframe_service: Annotated[WorkframeService, Depends(get_workframe_service)]
):
    try:
        workframe_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=400,detaif=f"Deu erro: {str(e)}")

@router.put("/update-mao-de-obra/{id_funcionario}")
def update_mao_de_obra(
    id_funcionario: str,
    salario: Annotated[float, Query()],
    cargo: Annotated[str, Query()],
    mao_de_obra_service: Annotated[MaoDeObraService, Depends(get_mao_de_obra_service)]
):
    try: 
        updated_mao_de_obra = mao_de_obra_service.update(id_funcionario, salario, cargo)
        if isinstance(updated_mao_de_obra, str):
            raise HTTPException(status_code=404, detail=updated_mao_de_obra)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.delete("/delete-mao-de-obra/{id_funcionario}")
def delete_mao_de_obra(
    id_funcionario:str,
    mao_de_obra_service: Annotated[MaoDeObraService, Depends(get_mao_de_obra_service)]
):
    try:
        result = mao_de_obra_service.delete(id_funcionario)
        if result is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id_funcionario}'não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    