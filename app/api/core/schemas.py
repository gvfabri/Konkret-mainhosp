from fastapi import Query
from pydantic import BaseModel
from typing import Annotated, Optional
from datetime import datetime

class ProprietarySchema(BaseModel):
    name: Annotated[str, Query()]
    cpf: Annotated[str, Query()]
    
    
class ProprietaryPublic(BaseModel):
    name: Annotated[str, Query()]
    id: Annotated[str, Query()]
    created_at: Annotated[datetime,Query()]
    updated_at: Annotated[datetime,Query()]
    class Config:
        orm_mode = True

class EmployeeSchema(BaseModel):
    name: Annotated[str, Query()]
    rg: Annotated[int, Query()]
    cpf: Annotated[int, Query()]
    role: Annotated[str, Query()]
    salary: Annotated[float, Query()]
    work_id: Annotated[Optional[str], Query(default=None)]

class EmployeePublic(BaseModel):
    name: Annotated[Optional[str], Query()]
    id: Annotated[str, Query()]
    role: Annotated[Optional[str], Query()]
    salary: Annotated[Optional[float], Query()]
    work_id: Annotated[Optional[str], Query(default=None)]

class UserSchema(BaseModel):
    name: Annotated[str, Query()]
    phone: Annotated[str, Query()] | None
    email: Annotated[str, Query()]
    password: Annotated[str, Query()]

class UserPublic(BaseModel):
    name: Annotated[str, Query()]
    phone: Annotated[str, Query()] | None
    email: Annotated[str, Query()]

class WorkSchema(BaseModel):
    address: Annotated[str, Query()]
    photos: Annotated[Optional[list], Query()]
    id_proprietary: Annotated[str, Query()]
    observations: Annotated[Optional[list], Query()]

class WorkPublic(BaseModel):
    address: Annotated[str, Query()]
    photos: Annotated[Optional[list], Query()]
    observations: Annotated[Optional[list], Query()]
    id: Annotated[str, Query()]
    proprietary_id: Annotated[str, Query()]
    created_at: Annotated[datetime,Query()]
    updated_at: Annotated[datetime,Query()]
    class Config:
        orm_mode = True

class PhotoSchema(BaseModel):
    id_work: Annotated[str, Query()]
    photo: Annotated[str, Query()]

class PhotoPublic(BaseModel):
    photo: Annotated[str, Query()]

class ObservationSchema(BaseModel):
    id_work: Annotated[str, Query()]
    observation: Annotated[str, Query()]

class ObservationPublic(BaseModel):
    observation: Annotated[str, Query()]

# Gustavo é hacker-man