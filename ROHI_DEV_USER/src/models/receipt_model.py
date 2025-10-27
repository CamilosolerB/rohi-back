from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum as SqlEnum, String
from sqlalchemy.orm import relationship
from enum import Enum
from src.utilities.db_user import Base

class ReceiptStatus(Enum):
    PENDING = "Pendiente"
    PAID = "Pagado"
    CANCELLED = "Cancelado"


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(SqlEnum(ReceiptStatus), default=ReceiptStatus.PENDING, nullable=False)
    url_receipt = Column(String(255), nullable=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)

    appointment = relationship("Appointment", back_populates="receipt")
