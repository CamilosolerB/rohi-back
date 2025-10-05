from pydantic import BaseModel

class UserCreateDTO(BaseModel):
    name: str
    email: str
    document_id: str
    document_type: str
    address: str
    phone_number: str
    sex: str
    
class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: str
