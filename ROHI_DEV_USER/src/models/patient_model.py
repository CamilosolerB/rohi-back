from sqlalchemy import Column, Integer, String, Boolean, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from src.utilities.db_user import Base
from src.models.appointmen_model import Appointment

class Eps(Enum):
    NE = "Nueva EPS"
    ST = "Salud Total"
    C = "Compensar"
    F = "Famisanar"


class Patient(Base):
    __tablename__ = "patients"

    id_pat = Column(Integer, primary_key=True, index=True, autoincrement=True)
    agent = Column(Boolean, nullable=False)
    name_agent = Column(String(255), nullable=True)
    phone_agent = Column(String(13), nullable=True)
    eps = Column(SqlEnum(Eps), nullable=False, default=Eps.F)
    user_document_id = Column(String(15), ForeignKey("users.document_id"), nullable=False, unique=True)
    # Relation with User
    user = relationship("User", back_populates="patient", uselist=False)
    # Relation with Appointment
    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete-orphan")
