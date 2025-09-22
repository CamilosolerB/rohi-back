from sqlalchemy import Column, String
from src.utilities.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    org_id = Column(String, index=True)
