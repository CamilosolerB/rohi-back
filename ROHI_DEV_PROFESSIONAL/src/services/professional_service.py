from typing import Optional, List
from src.dto.professional_dto import ProfessionalDTO
from src.repositories.professional_repository import ProfessionalRepository
from src.utilities.db_professional import get_session

class ProfessionalService:
    def __init__(self):
        self.db = get_session()
        self.repo = ProfessionalRepository(self.db)

    def create_professional(self, data) -> ProfessionalDTO:
        professional = self.repo.create(data)
        return ProfessionalDTO.from_orm(professional)
    
    def list_professionals(self) -> List[ProfessionalDTO]:
        professionals = self.repo.get_all()
        return [ProfessionalDTO.from_orm(professional) for professional in professionals]
    
    def update_professional(self, user_document_id: str, **kwargs) -> Optional[ProfessionalDTO]:
        patient = self.repo.update(user_document_id, **kwargs)
        return ProfessionalDTO.from_orm(patient)
    
    def get_professional(self, user_document_id: str) -> Optional[ProfessionalDTO]:
        patient = self.repo.get_by_id(user_document_id)
        return ProfessionalDTO.from_orm(patient)

    def delete_professional(self, user_document_id: int) -> bool:
        return self.repo.delete(user_document_id)
