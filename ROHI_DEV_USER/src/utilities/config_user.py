import os

class Config:
    DB_USER = os.getenv("DB_USER", "admin")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "RohiIPS2025")  
    DB_HOST = os.getenv("DB_HOST", "database-rohi.cu16ogsoolsh.us-east-1.rds.amazonaws.com")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "rohi_db")

    DATABASE_URL = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
