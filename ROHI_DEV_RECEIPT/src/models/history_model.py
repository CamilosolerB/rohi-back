from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, TEXT
from sqlalchemy.orm import relationship
from enum import Enum
from src.utilities.db_receipt import Base

class History(Base):
    __tablename__ = "histories"

    id_hist = Column(Integer, primary_key=True, index=True, autoincrement=True)
    background = Column(TEXT, nullable=False)
    diagnostic = Column(TEXT, nullable=False)
    manage_plan = Column(TEXT, nullable=False)
    treatment = Column(TEXT, nullable=False)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)

    appointment = relationship("Appointment", back_populates="history", uselist=False)