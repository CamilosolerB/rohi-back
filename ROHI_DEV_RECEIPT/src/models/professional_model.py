from sqlalchemy import Column, Integer, String, Boolean, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from src.utilities.db_receipt import Base
from src.models.appointmen_model import Appointment

class Professional(Base):
    __tablename__ = "professionals"
    id_prof = Column(Integer, primary_key=True, index=True, autoincrement=True)
    profession = Column(String(255), nullable=False)
    specialty = Column(String(255), nullable=False)
    vehicle = Column(Boolean, nullable=False)
    plate_vehicle = Column(String(10), nullable=True)
    city = Column(String(255), nullable=False)
    user_document_id = Column(String(15), ForeignKey("users.document_id"), nullable=False, unique=True)
    user = relationship("User", back_populates="professional", uselist=False)
    appointments = relationship("Appointment", back_populates="professional", cascade="all, delete-orphan")