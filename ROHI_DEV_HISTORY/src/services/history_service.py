from src.dto.history_dto import HistoryDTO
from src.repositories.history_repository import HistoryRepository
from src.utilities.db_history import get_session

class HistoryService:
    def __init__(self):
        self.db = get_session()
        self.repo = HistoryRepository(self.db)

    def create_history(self, history_data: HistoryDTO):
        new_history = self.repo.create_history(history_data)
        self.db.commit()
        self.db.refresh(new_history)
        return new_history
    
    def get_history(self, history_id: int):
        return self.repo.get_history(history_id)
    
    def update_history(self, history_id: int, history_data: HistoryDTO):
        return self.repo.update_history(history_id, history_data)
    
    def delete_history(self, history_id: int):
        return self.repo.delete_history(history_id)