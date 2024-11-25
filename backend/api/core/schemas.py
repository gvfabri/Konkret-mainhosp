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
    name: Annotated[Optional[str], Query()]
    rg: Annotated[int, Query()]
    cpf: Annotated[int, Query()]
    role: Annotated[Optional[str], Query()]
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
    cpf: Annotated[str, Query()] | None
    email: Annotated[str, Query()]
    password: Annotated[str, Query()]

class UserPublic(BaseModel):
    name: Annotated[str, Query()]
    cpf: Annotated[str, Query()] | None
    email: Annotated[str, Query()]

class LoginSchema(BaseModel):
    email: str
    password: str

class WorkSchema(BaseModel):
    address: Annotated[str, Query()]
    photos: Annotated[Optional[list], Query()]
    id_proprietary: Annotated[str, Query()]
    observations: Annotated[Optional[list], Query()]
    activities: Annotated[Optional[list], Query()]

class WorkPublic(BaseModel):
    address: Annotated[str, Query()]
    photos: Annotated[Optional[list], Query()]
    observations: Annotated[Optional[list], Query()]
    id: Annotated[str, Query()]
    proprietary_id: Annotated[str, Query()]
    activities: Annotated[Optional[list], Query()]
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

class ActivitySchema(BaseModel):
    id_work: Annotated[str, Query()]
    activity: Annotated[str, Query()]

class ActivityPublic(BaseModel):
    activity: Annotated[str, Query()]

class ClimateSchema(BaseModel):
    id_work: Annotated[str, Query()]

class ClimatePublic(BaseModel):
    temperature: Annotated[float, Query()]
    pressure: Annotated[float, Query()]
    humidity: Annotated[float, Query()]
    wind_speed: Annotated[float, Query()]
    visibility: Annotated[float, Query()]
# Gustavo é hacker-man