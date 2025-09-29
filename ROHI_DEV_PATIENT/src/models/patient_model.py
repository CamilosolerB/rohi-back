from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fullname = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    documentId = Column(String(20), unique=True, nullable=False)
    phoneNumber = Column(String(20), nullable=False)
    age = Column(Integer, nullable=True)
