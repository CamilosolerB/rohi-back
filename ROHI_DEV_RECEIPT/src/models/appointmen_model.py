from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SqlEnum, Boolean
from sqlalchemy.orm import relationship
from enum import Enum
from src.utilities.db_receipt import Base
from src.models.history_model import History
from src.models.receipt_model import Receipt

class AppointmentStatus(Enum):
    FREE = "free"
    NOT_PAYED = "not_paid"
    PAYED = "payed"
    ON_PROGRESS = "on_progress"
    FINISHED = "finished"


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    care_type = Column(Boolean, nullable=False)
    app_type = Column(Boolean, nullable=False)
    status = Column(SqlEnum(AppointmentStatus), default=AppointmentStatus.FREE, nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id_pat"), nullable=True)
    professional_id = Column(Integer, ForeignKey("professionals.id_prof"), nullable=False)

    patient = relationship("Patient", back_populates="appointments")
    professional = relationship("Professional", back_populates="appointments")
