from src.models.receipt_model import Receipt
from sqlalchemy.orm import Session
from src.dto.receipt_dto import ReceiptDTO
from src.utilities.mailer import send_payment_email
from src.utilities.reportMaker import generate_clinical_report

class ReceiptRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_receipt(self, body, patient_email: str):
        receipt = Receipt(**body)
        self.session.add(receipt)
        self.session.commit()

        success = send_payment_email(patient_email)

        if not success:
            raise Exception("Failed to send payment email")

        return receipt
    
    def get_receipt_by_id(self, receipt_id: int):
        return self.session.query(Receipt).filter(Receipt.id == receipt_id).first()
    
    def get_all_receipts(self):
        return self.session.query(Receipt).all()
    
    def delete_receipt(self, receipt_id: int):
        receipt = self.get_receipt_by_id(receipt_id)
        if receipt:
            self.session.delete(receipt)
            self.session.commit()
    def update_receipt(self, body, receipt_id: int):
        receipt = self.get_receipt_by_id(receipt_id)
        if receipt:
            for key, value in body.items():
                setattr(receipt, key, value)
            self.session.commit()
        return receipt
    
    def complete_receipt_payment(self, body):
        receipt = self.get_receipt_by_id(body["receipt_id"])
        if not receipt:
            raise Exception("Receipt not found")

        receipt.status = "Pagado"
        url = generate_clinical_report(receipt.appointment_id)
        receipt.url_receipt = url
        self.session.commit()
        return receipt