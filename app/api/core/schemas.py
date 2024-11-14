from fastapi import Query
from pydantic import BaseModel
from typing import Annotated
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