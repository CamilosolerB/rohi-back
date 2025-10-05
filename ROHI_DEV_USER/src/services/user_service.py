from src.dto.user_dto import UserCreateDTO, UserResponseDTO
from src.repositories.user_repository import UserRepository
from src.utilities.db_user import get_session

class UserService:
    def __init__(self):
        self.db = get_session()
        self.repo = UserRepository(self.db)

    def create_user(self, data):
        user = self.repo.create(data)
        return user 

    def get_user(self, user_id: int) -> UserResponseDTO | None:
        user = self.repo.get_by_id(user_id)
        if not user:
            return None
        return UserResponseDTO(id=user.id, name=user.name, email=user.email)
