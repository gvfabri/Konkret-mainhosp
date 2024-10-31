from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, func, JSON
from sqlalchemy.orm import relationship, declarative_base
from uuid import uuid4
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True,default=lambda: str(uuid4()))
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Proprietary(Base):
    __tablename__ = "proprietaries"

    id = Column(String, primary_key=True, index=True,default=lambda: str(uuid4()))
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

