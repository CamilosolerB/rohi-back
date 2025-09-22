from typing import Optional, List
from sqlalchemy.orm import Session
from src.models.user import User
from src.dto.user_dto import UserDTO

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: str) -> Optional[UserDTO]:
        user = self.db.query(User).filter(User.id == user_id).first()
        return UserDTO(**user.__dict__) if user else None

    def create(self, dto: UserDTO) -> UserDTO:
        user = User(**dto.__dict__)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return UserDTO(**user.__dict__)

    def list_by_org(self, org_id: str) -> List[UserDTO]:
        users = self.db.query(User).filter(User.org_id == org_id).all()
        return [UserDTO(**u.__dict__) for u in users]

    def delete(self, user_id: str) -> None:
        self.db.query(User).filter(User.id == user_id).delete()
        self.db.commit()
