from pydantic import BaseModel, field_serializer
from datetime import datetime
from typing import Optional

class AppointmentDTO(BaseModel):
    id: int
    date: datetime
    care_type: bool
    app_type: bool
    status: str
    patient_id: Optional[int]
    professional_id: int

    class Config:
        from_attributes = True
        use_enum_values = True

    @field_serializer("date")
    def serialize_date(self, date: datetime, _info):
        return date.isoformat()