from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_sqlalchemy import SQLAlchemy


DATABASE_URL = 'postgresql://root:secret@127.0.0.1:5434/iotmanagement'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

db = SQLAlchemy()

def get_db_session():
    db_session = SessionLocal()

    try:
        yield db_session
    finally:
        db_session.close()
