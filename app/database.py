from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# import psycopg2
# import time
# from psycopg2.extras import RealDictCursor

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Uncomment the following lines if you want to use psycopg2 for direct database connection
# # Initialize database connection

# try:
#     conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='password123', cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection successful")
# except Exception as error:
#     print("Database connection failed")
#     print(f"Error: {error}")
#     time.sleep(2)
