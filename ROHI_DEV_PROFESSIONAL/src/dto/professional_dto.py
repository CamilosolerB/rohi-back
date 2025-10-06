from pydantic import BaseModel

class ProfessionalDTO(BaseModel):
    user_document_id: str
    id_prof: int
    profession: str
    specialty: str
    vehicle: bool
    plate_vehicle: str | None
    city: str

    class Config:
        from_attributes = True
        use_enum_values = True