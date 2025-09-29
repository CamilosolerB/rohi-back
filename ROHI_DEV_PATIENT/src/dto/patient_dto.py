from pydantic import BaseModel, EmailStr
from typing import Optional

class PatientDTO(BaseModel):
    id: Optional[int] = None   # Se llena al devolver desde DB
    fullname: str
    email: EmailStr
    documentId: str
    phoneNumber: str
    age: Optional[int] = None
