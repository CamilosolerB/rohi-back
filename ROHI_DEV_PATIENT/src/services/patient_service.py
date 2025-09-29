from typing import Optional, List
from ROHI_DEV_PATIENT.src.dto.patient_dto import PatientDTO
from ROHI_DEV_PATIENT.src.repositories.patient_repository import PatientRepository
from ROHI_DEV_PATIENT.src.utilities.db_patient import get_session

class PatientService:
    def __init__(self):
        self.db = get_session()
        self.repo = PatientRepository(self.db)

    def create_patient(self, data: PatientDTO) -> PatientDTO:
        patient = self.repo.create(
            fullname=data.fullname,
            email=data.email,
            documentId=data.documentId,
            phoneNumber=data.phoneNumber,
            age=data.age
        )
        return PatientDTO(
            id=patient.id,
            fullname=patient.fullname,
            email=patient.email,
            documentId=patient.documentId,
            phoneNumber=patient.phoneNumber,
            age=patient.age
        )

    def get_patient(self, patient_id: int) -> Optional[PatientDTO]:
        patient = self.repo.get_by_id(patient_id)
        if not patient:
            return None
        return PatientDTO(
            id=patient.id,
            fullname=patient.fullname,
            email=patient.email,
            documentId=patient.documentId,
            phoneNumber=patient.phoneNumber,
            age=patient.age
        )

    def list_patients(self) -> List[PatientDTO]:
        patients = self.repo.get_all()
        return [
            PatientDTO(
                id=p.id,
                fullname=p.fullname,
                email=p.email,
                documentId=p.documentId,
                phoneNumber=p.phoneNumber,
                age=p.age
            )
            for p in patients
        ]

    def update_patient(self, patient_id: int, data: PatientDTO) -> Optional[PatientDTO]:
        updated = self.repo.update(
            patient_id,
            fullname=data.fullname,
            email=data.email,
            documentId=data.documentId,
            phoneNumber=data.phoneNumber,
            age=data.age
        )
        if not updated:
            return None
        return PatientDTO(
            id=updated.id,
            fullname=updated.fullname,
            email=updated.email,
            documentId=updated.documentId,
            phoneNumber=updated.phoneNumber,
            age=updated.age
        )

    def delete_patient(self, patient_id: int) -> bool:
        return self.repo.delete(patient_id)
