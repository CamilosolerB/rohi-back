from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config_patient import Config

# Crear engine con la URL de la base de datos desde config
engine = create_engine(
    Config.DATABASE_URL,
    pool_pre_ping=True,   # Evita errores de conexión si la conexión se cae
    echo=False            # Cambia a True para ver los logs SQL
)

# Crear sesión
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_session():
    return SessionLocal()
