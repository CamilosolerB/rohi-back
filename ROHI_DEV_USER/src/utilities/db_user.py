from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config_user import Config

engine = create_engine(
    Config.DATABASE_URL,
    pool_pre_ping=True,  
    echo=False            
)

# Crear sesión
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_session():
    return SessionLocal()
