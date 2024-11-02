from fastapi import APIRouter, Request, Query, Depends, HTTPException
from typing import Annotated
from ...services.user_service import UserService
from ...services.mao_de_obra_service import MaoDeObraService
from ...dependencies import get_user_service, get_mao_de_obra_service

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


@router.put("/update-mao-de-obra/{id_funcionario}")
def update_mao_de_obra(
    id_funcionario: str,
    salario: Annotated[float, Query(default=None)],
    cargo: Annotated[str, Query(default=None)],
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
    