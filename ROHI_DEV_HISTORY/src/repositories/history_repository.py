from src.models.history_model import History
from sqlalchemy.orm import Session

class HistoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_history(self, history_data: History) -> History:
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
    
    def update_history(self, history_id: int, history_data: History) -> History:
        history = self.get_history(history_id)
        if history:
            history.background = history_data.background
            history.diagnostic = history_data.diagnostic
            history.manage_plan = history_data.manage_plan
            history.treatment = history_data.treatment
            history.appointment_id = history_data.appointment_id
            self.db.commit()
        return history
    
    def delete_history(self, history_id: int) -> bool:
        history = self.get_history(history_id)
        if history:
            self.db.delete(history)
            self.db.commit()
            return True
        return False
    