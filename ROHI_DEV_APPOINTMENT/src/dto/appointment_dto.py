from pydantic import BaseModel

class Appointment:
    id: int
    date: str
    care_type: bool
    app_type: bool
    status: str
    patient_id: int | None
    professional_id: int

    class Config:
        from_attributes = True
        use_enum_values = True