from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, func, JSON
from sqlalchemy.orm import relationship, declarative_base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import ARRAY
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
    __tablename__ = "proprietary"

    id = Column(String, primary_key=True, index=True,default=lambda: str(uuid4()))
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Employee(Base):
    __tablename__ = "employees"

    id = Column(String, primary_key=True, index=True,default=lambda: str(uuid4()))
    name = Column(String, nullable=True)
    rg = Column(Integer, nullable=True)
    cpf = Column(Integer, nullable=False)
    role = Column(String, nullable=True)
    salary = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Work(Base):
    __tablename__ = 'works'
    id = Column(String, primary_key=True, index=True,default=lambda: str(uuid4()))
    address = Column(String, nullable=False)
    photos = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())