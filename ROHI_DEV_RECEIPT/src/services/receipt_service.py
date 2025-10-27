
from src.repositories.receipt_repository import ReceiptRepository
from src.utilities.db_receipt import get_session

class UserService:
    def __init__(self):
        self.db = get_session()
        self.repo = ReceiptRepository(self.db)

    def create_receipt(self, body, patient_email: str):
        receipt = self.repo.add_receipt(body, patient_email)
        return receipt
    
    def get_receipt(self, receipt_id: int):
        receipt = self.repo.get_receipt_by_id(receipt_id)
        return receipt
    
    def get_all_receipts(self):
        receipts = self.repo.get_all_receipts()
        return receipts
    
    def update_receipt(self, receipt_id: int, **body):
        receipt = self.repo.update_receipt(body, receipt_id)
        return receipt
    
    def delete_receipt(self, receipt_id: int):
        self.repo.delete_receipt(receipt_id)
    def complete_receipt_payment(self, body):
        receipt = self.repo.complete_receipt_payment(body)
        return receipt
    
