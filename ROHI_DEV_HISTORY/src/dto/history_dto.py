from pydantic import BaseModel

class HistoryDTO(BaseModel):
    id_hist: int
    background: str
    diagnostic: str
    manage_plan: str
    treatment: str
    appointment_id: int
    class Config:
        from_attributes = True
        use_enum_values = True