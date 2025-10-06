from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config_patient import Config

# Crear engine con la URL de la base de datos desde config
engine = create_engine(
    Config.DATABASE_URL,
    pool_pre_ping=True,   # Evita errores de conexión si la conexión se cae
    echo=False            # Cambia a True para ver los logs SQL
)

# Crear sesión
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
for table in Base.metadata.tables:
    print(table)

def get_session():
    return SessionLocal()
