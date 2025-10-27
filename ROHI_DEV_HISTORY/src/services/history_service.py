from src.repositories.history_repository import HistoryRepository
from src.utilities.db_history import get_session

class HistoryService:
    def __init__(self):
        self.db = get_session()
        self.repo = HistoryRepository(self.db)

    def create_history(self, body):
        new_history = self.repo.create_history(body)
        self.db.commit()
        self.db.refresh(new_history)
        return new_history
    
    def get_history(self, history_id: int):
        return self.repo.get_history(history_id)
    
    def update_history(self, history_id: int, body):
        return self.repo.update_history(history_id, body)
    
    def delete_history(self, history_id: int):
        return self.repo.delete_history(history_id)