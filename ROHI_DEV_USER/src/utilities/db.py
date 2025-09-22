from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from src.utilities.config import Config

Base = declarative_base()

# Engine reutilizable (Lambda lo mantiene entre invocaciones)
engine = create_engine(Config.DATABASE_URL, pool_size=2, max_overflow=5)

SessionLocal = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
