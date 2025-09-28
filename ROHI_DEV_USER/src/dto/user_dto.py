from pydantic import BaseModel

class UserCreateDTO(BaseModel):
    name: str
    email: str

class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: str
