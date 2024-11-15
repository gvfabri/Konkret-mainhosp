from fastapi import APIRouter, HTTPException, Depends
from app.api.core.schemas import ProprietarySchema, ProprietaryPublic
from typing import Annotated, List
from app.api.services.proprietary_service import ProprietaryService
from app.api.dependencies import get_proprietary_service

router = APIRouter(
    prefix="/proprietary",
    tags=["Proprietary"],
)

@router.post("", response_model=ProprietaryPublic)
def add_proprietary(
    proprietary: ProprietarySchema,
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        return proprietary_service.create_proprietary(proprietary.name,proprietary.cpf)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")

@router.get("", response_model=List[ProprietaryPublic])
def getall_proprietaries(
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        return proprietary_service.all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}", response_model=ProprietaryPublic)
def get_proprietary(
    id: str,
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        proprietary = proprietary_service.get(id)
        if proprietary is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
        return proprietary
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")
    
@router.delete("/{id}", response_model=ProprietaryPublic)
def delete_proprietary(
    id:str,
    proprietary_service: Annotated[ProprietaryService, Depends(get_proprietary_service)]
):
    try:
        result = proprietary_service.delete(id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"ID: '{id}'não encontrado.")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")