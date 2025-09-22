from typing import Optional, List
from src.dto.user_dto import UserDTO
from src.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_user(self, user_id: str) -> Optional[UserDTO]:
        return self.repo.get_by_id(user_id)

    def create_user(self, dto: UserDTO) -> UserDTO:
        if "@" not in dto.email:
            raise ValueError("Invalid email format")
        return self.repo.create(dto)

    def list_users_by_org(self, org_id: str) -> List[UserDTO]:
        return self.repo.list_by_org(org_id)

    def delete_user(self, user_id: str):
        self.repo.delete(user_id)
