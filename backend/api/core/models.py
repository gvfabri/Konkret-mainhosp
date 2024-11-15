from sqlalchemy import Table, Column, String, Float, Integer, Text, ForeignKey, DateTime, func, JSON
from sqlalchemy.orm import relationship, declarative_base, mapped_column, Mapped
from uuid import uuid4
from sqlalchemy.dialects.postgresql import ARRAY
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id: Mapped[String] = mapped_column(String, primary_key=True, index=True,default=lambda: str(uuid4()))
    name = mapped_column(String, nullable=False)
    cpf = mapped_column(String, nullable=True)
    email = mapped_column(String, nullable=False, unique=True)
    password = mapped_column(String, nullable=True)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Proprietary(Base):
    __tablename__ = "proprietaries"

    id: Mapped[String] = mapped_column(String, primary_key=True, index=True,default=lambda: str(uuid4()))
    name = mapped_column(String, nullable=False)
    cpf = mapped_column(String, nullable=False, unique=True)
    works = relationship("Work", back_populates="proprietary")
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[String] = mapped_column(String, primary_key=True, index=True,default=lambda: str(uuid4()))
    name = mapped_column(String, nullable=True)
    rg = mapped_column(Integer, nullable=True, unique=True)
    cpf = mapped_column(Integer, nullable=False, unique=True)
    role = mapped_column(String, nullable=True)
    salary = mapped_column(Float, nullable=False)
    work_id = mapped_column(ForeignKey("works.id"), nullable=True)
    work = relationship("Work", back_populates="workers")
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Work(Base):
    __tablename__ = 'works'

    id: Mapped[String] = mapped_column(String, primary_key=True, index=True,default=lambda: str(uuid4()))
    address = mapped_column(String, nullable=False)
    photos = mapped_column(ARRAY(String), nullable=True)
    proprietary_id = mapped_column(ForeignKey("proprietaries.id"), nullable=False)
    proprietary = relationship("Proprietary", back_populates="works")
    observations = mapped_column(ARRAY(Text), nullable=True)
    workers = relationship("Employee", back_populates="work")
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())