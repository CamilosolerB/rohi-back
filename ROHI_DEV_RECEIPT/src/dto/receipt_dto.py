from pydantic import BaseModel

class ReceiptDTO(BaseModel):
    id_receipt: int
    date: str
    total_amount: float
    status: str
    url_receipt: str
    appointment_id: int

    class Config:
        from_attributes = True
        use_enum_values = True