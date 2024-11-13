from fastapi import APIRouter, Request, Query, Depends, HTTPException
from typing import Annotated
from app.api.services.user_service import UserService
from app.api.dependencies import get_user_service
from app.api.utils import is_valid_password

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("")
def add_user(
    name: Annotated[str, Query()],
    phone: Annotated[str, Query()],
    email: Annotated[str, Query()],
    password: Annotated[str, Query()],
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    password_error = is_valid_password(password)
    if password_error:
        raise HTTPException(status_code=400, detail=password_error)

    try:
        user = user_service.create_user(name,phone,email, password)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")

@router.put("/{id}/update")
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
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")

@router.get("")
def getall_users(
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        return user_service.all()
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}")
def get_user(
    id: str,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        return user_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.delete("/{id}")
def delete_user(
    id: str,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        user_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")