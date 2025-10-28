from pydantic import BaseModel


class PatientDTO(BaseModel):
    id_pat: int
    agent: bool
    name_agent: str | None
    phone_agent: str | None
    eps: str

    class Config:
        from_attributes = True
        use_enum_values = True