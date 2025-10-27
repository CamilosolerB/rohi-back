from src.models.history_model import History
from src.dto.history_dto import HistoryDTO
from sqlalchemy.orm import Session

class HistoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_history(self, body) -> History:
        history_data = HistoryDTO(**body)
        new_history = History(
            background=history_data.background,
            diagnostic=history_data.diagnostic,
            manage_plan=history_data.manage_plan,
            treatment=history_data.treatment,
            appointment_id=history_data.appointment_id
        )
        self.db.add(new_history)
        return new_history
    
    def get_history(self, history_id: int) -> History:
        return self.db.query(History).filter(History.id_hist == history_id).first()
    
    def update_history(self, history_id: int, body) -> History:
        history = self.get_history(history_id)
        if history:
            for key, value in body.items():
                setattr(history, key, value)
            self.db.commit()
            self.db.refresh(history)
        return history
    
    def delete_history(self, history_id: int) -> bool:
        history = self.get_history(history_id)
        if history:
            self.db.delete(history)
            self.db.commit()
            return True
        return False
    