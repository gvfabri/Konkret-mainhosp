from fastapi import APIRouter, Request, Query, Depends, HTTPException
from typing import Annotated
from ...services.user_service import UserService
from ...dependencies import get_user_service

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