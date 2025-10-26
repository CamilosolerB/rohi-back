from src.dto.user_dto import UserDTO
from src.repositories.user_repository import UserRepository
from src.utilities.db_user import get_session

class UserService:
    def __init__(self):
        self.db = get_session()
        self.repo = UserRepository(self.db)

    def create_user(self, data):
        user = self.repo.create(data)
        return UserDTO.from_orm(user) 
    
    def get_all_users(self):
        users = self.repo.get_all_users()
        return [UserDTO.from_orm(user) for user in users]

    def get_user(self, user_id: int) -> UserDTO:
        user = self.repo.get_by_id(user_id)
        if not user:
            return None
        return UserDTO.from_orm(user)
    
    def get_user_by_email(self, email: str) -> UserDTO:
        user = self.repo.get_by_email(email)
        if not user:
            return None
        return UserDTO.from_orm(user)
    
    def update_user(self, user_id: str, **kwargs) -> UserDTO:
        user = self.repo.update_by_id(user_id, **kwargs)
        if not user:
            return None
        return UserDTO.from_orm(user)
    
    def delete_user(self, user_id: str) -> UserDTO:
        user = self.repo.delete_by_id(user_id)
        if not user:
            return None
        return UserDTO.from_orm(user)
