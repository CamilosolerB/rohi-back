from ROHI_DEV_PATIENT.src.models.patient_model import Patient
from sqlalchemy.orm import Session
from typing import Optional, List

class PatientRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, fullname: str, email: str, documentId: str, phoneNumber: str, age: int | None = None) -> Patient:
        patient = Patient(
            fullname=fullname,
            email=email,
            documentId=documentId,
            phoneNumber=phoneNumber,
            age=age
        )
        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient

    def get_by_id(self, patient_id: int) -> Optional[Patient]:
        return self.db.query(Patient).filter(Patient.id == patient_id).first()

    def get_all(self) -> List[Patient]:
        return self.db.query(Patient).all()

    def update(self, patient_id: int, **kwargs) -> Optional[Patient]:
        patient = self.get_by_id(patient_id)
        if not patient:
            return None
        for key, value in kwargs.items():
            if hasattr(patient, key) and value is not None:
                setattr(patient, key, value)
        self.db.commit()
        self.db.refresh(patient)
        return patient

    def delete(self, patient_id: int) -> bool:
        patient = self.get_by_id(patient_id)
        if not patient:
            return False
        self.db.delete(patient)
        self.db.commit()
        return True
