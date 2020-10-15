from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


HOST = "db"
DATABASE = "test_database"
USER = "root"
PASSWORD = "root"

SQLALCHEMY_DB_URL = f"mysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8"
# pymysql なら pure Python らしい f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8"
engine = create_engine(
    SQLALCHEMY_DB_URL,
    connect_args={},
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
