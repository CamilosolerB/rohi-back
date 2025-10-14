from pydantic import BaseModel

class UserDTO(BaseModel):
    name: str
    email: str
    document_id: str
    document_type: str
    address: str
    phone_number: str
    sex: str
    
    class Config:
        from_attributes = True
        use_enum_values = True