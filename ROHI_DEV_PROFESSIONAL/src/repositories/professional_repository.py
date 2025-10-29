from src.models.professional_model import Professional
from sqlalchemy.orm import Session
from typing import Optional, List

class ProfessionalRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, body) -> Professional:
        try:
            professional = Professional(**body)
            self.db.add(professional)
            self.db.commit()
            self.db.refresh(professional)
            return professional
        except Exception as e:
            raise e

    def get_by_id(self, user_document_id: str) -> Optional[Professional]:
        return self.db.query(Professional).filter(Professional.id_prof == user_document_id).first()

    def get_all(self) -> List[Professional]:
        return self.db.query(Professional).all()

    def update(self, user_document_id: str, **kwargs) -> Optional[Professional]:
        patient = self.get_by_id(user_document_id)
        if not patient:
            return None
        for key, value in kwargs.items():
            if hasattr(patient, key) and value is not None:
                setattr(patient, key, value)
        self.db.commit()
        self.db.refresh(patient)
        return patient

    def delete(self, user_document_id: str) -> bool:
        patient = self.get_by_id(user_document_id)
        if not patient:
            return False
        self.db.delete(patient)
        self.db.commit()
        return True
