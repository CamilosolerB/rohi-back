from typing import Optional, List
from src.dto.patient_dto import PatientDTO
from src.repositories.patient_repository import PatientRepository
from src.utilities.db_patient import get_session

class PatientService:
    def __init__(self):
        self.db = get_session()
        self.repo = PatientRepository(self.db)

    def create_patient(self, data) -> PatientDTO:
        patient = self.repo.create(data)
        return PatientDTO.from_orm(patient)
    
    def list_patients(self) -> List[PatientDTO]:
        patients = self.repo.get_all()
        return [PatientDTO.from_orm(patient) for patient in patients]
    
    def update_patient(self, user_document_id: str, **kwargs) -> Optional[PatientDTO]:
        patient = self.repo.update(user_document_id, **kwargs)
        return PatientDTO.from_orm(patient)
    
    def get_patient(self, user_document_id: str) -> Optional[PatientDTO]:
        patient = self.repo.get_by_id(user_document_id)
        return PatientDTO.from_orm(patient)

    def delete_patient(self, user_document_id: int) -> bool:
        return self.repo.delete(user_document_id)
