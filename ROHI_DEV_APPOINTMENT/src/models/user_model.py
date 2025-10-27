from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from src.utilities.db_appointment import Base
from sqlalchemy.orm import relationship
from enum import Enum

class DocumentType(Enum):
    CC = "CC"
    CE = "CE"
    TI = "TI"
    PP = "PP"
    RC = "RC"

class Sex(Enum):
    M = "Masculino"
    F = "Feminino"
    NB = "No Binario"
    TS = "Transexual"
    NN = "No se identifica con los anteriores"

class Rol(Enum):
    GERENTE = "Gerente"
    ADMIN = "Administrador"
    DOCTOR = "Doctor"
    TERAPEUTA = "Terapeuta"
    PACIENTE = "Paciente"

class User(Base):
    __tablename__ = "users"

    document_id = Column(String(15), primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True)
    document_type = Column(SqlEnum(DocumentType), default=DocumentType.CC, nullable=False)
    address = Column(String(200), nullable=False)
    phone_number = Column(String(13), nullable=False)
    sex = Column(SqlEnum(Sex), default=Sex.M, nullable=False)
    rol = Column(SqlEnum(Rol), default=Rol.PACIENTE, nullable=False)
    is_active = Column(Integer, default=1, nullable=False)
    patient = relationship("Patient", back_populates="user", uselist=False)
    professional = relationship("Professional", back_populates="user", uselist=False)

from src.models.professional_model import Professional
