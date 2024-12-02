from fastapi import APIRouter, HTTPException, Depends
from backend.api.core.models import User
from backend.api.core.schemas import ProprietarySchema, ProprietaryPublic, WorkPublic
from typing import Annotated, List
from backend.api.services.proprietary_service import ProprietaryService
from backend.api.dependencies import get_proprietary_service, get_current_user

router = APIRouter(
    prefix="/proprietary",
    tags=["Proprietary"],
)

@router.post("", response_model=ProprietaryPublic)
def add_proprietary(
    proprietary: ProprietarySchema,
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)],
    user_logged: User = Depends(get_current_user)
):
    if not user_logged:
        raise HTTPException(status_code=404, detail="Usuário logado não encontrado.")
    try:
        return proprietary_service.create_proprietary(proprietary.name,proprietary.cpf)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")

@router.get("", response_model=List[ProprietaryPublic])
def getall_proprietaries(
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)], 
    user_logged: User = Depends(get_current_user)
):
    if not user_logged:
        raise HTTPException(status_code=404, detail="Usuário logado não encontrado.")
    try:
        return proprietary_service.all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}", response_model=ProprietaryPublic)
def get_proprietary(
    id: str,
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)],
    user_logged: User = Depends(get_current_user)
):
    if not user_logged:
        raise HTTPException(status_code=404, detail="Usuário logado não encontrado.")
    try:
        proprietary = proprietary_service.get(id)
        if proprietary is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
        return proprietary
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}/works", response_model=List[WorkPublic])
def get_works(
    id: str,
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)],
    user_logged: User = Depends(get_current_user)
):
    if not user_logged:
        raise HTTPException(status_code=404, detail="Usuário logado não encontrado.")
    try:
        works = proprietary_service.works(id)
        if works is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
        return works
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.delete("/{id}", response_model=ProprietaryPublic)
def delete_proprietary(
    id:str,
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)],
    user_logged: User = Depends(get_current_user)
):
    if not user_logged:
        raise HTTPException(status_code=404, detail="Usuário logado não encontrado.")
    try:
        result = proprietary_service.delete(id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")