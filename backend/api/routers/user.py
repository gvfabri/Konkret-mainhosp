from fastapi import APIRouter, Request, Query, Depends, HTTPException
from typing import Annotated, List
from backend.api.services.user_service import UserService
from backend.api.core.schemas import UserSchema, UserPublic, LoginSchema
from backend.api.dependencies import get_user_service
from backend.api.utils import is_valid_password, is_valid_cpf, verificar_senha

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("", response_model=UserPublic)
def add_user(
    user: UserSchema,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    password_error = is_valid_password(user.password)
    if password_error:
        raise HTTPException(status_code=400, detail=password_error)
    
    # Valida o CPF
    if not is_valid_cpf(user.cpf):
        raise HTTPException(status_code=400, detail="CPF inválido.")

    try:
        return user_service.create_user(user.name,user.cpf,user.email, user.password)        

    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")

@router.put("/{id}/update", response_model=UserPublic)
def update_user(
    id: str,
    user: UserSchema,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try: 
        updated_user = user_service.update(id, user.phone, user.email, user.password)
        if isinstance(updated_user, str):
            raise HTTPException(status_code=404)
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")

@router.get("", response_model=List[UserPublic])
def getall_users(
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        return user_service.all()
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}", response_model=UserPublic)
def get_user(
    id: str,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        return user_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.delete("/{id}", response_model=UserPublic)
def delete_user(
    id: str,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        return user_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.post("/login")
def login(
    credentials: LoginSchema,
    user_service: Annotated[UserService, Depends(get_user_service)]
):
    # Tenta buscar o usuário pelo e-mail ou CPF
    user = user_service.find_by_email(credentials.email)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")

    # Verifica se a senha está correta
    if not verificar_senha(credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")
    return "Usuário aceito para ser logado"
