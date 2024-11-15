from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Annotated
from backend.api.services.proprietary_service import ProprietaryService
from backend.api.dependencies import get_proprietary_service

router = APIRouter(
    prefix="/proprietary",
    tags=["Proprietary"],
)

@router.post("")
def add_proprietary(
    name: Annotated[str, Query()],
    cpf: Annotated[str, Query()],
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        return proprietary_service.create_proprietary(name,cpf)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")

@router.get("")
def getall_proprietaries(
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        return proprietary_service.all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}")
def get_proprietary(
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        proprietary = proprietary_service.get(id)
        if proprietary is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
        return proprietary
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.delete("/{id}")
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