from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./db.sqlite3"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass