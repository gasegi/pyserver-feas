import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

from database.database import Base
from test.testdata import initializeTestData


@pytest.fixture(scope="function")
def SessionLocal(request):
    # get test-name
    testid1 = os.environ.get('PYTEST_CURRENT_TEST').split(
        ':')[-1].split(' ')[0].strip('[]')
    testid2 = request.node.name
    testid3 = request.node.originalname
    testid4 = request.module.__name__
    print('test id', testid1, testid2, testid3, testid4)

    # settings of test database
    HOST = "db"
    DATABASE = "test_test_database"
    USER = "root"
    PASSWORD = "root"

    SQLALCHEMY_DB_URL = f"mysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8"
    engine = create_engine(SQLALCHEMY_DB_URL,
                           connect_args={})

    # yield SessionLocal で失敗した時後続処理が動かない問題があるらしく、下のコードは問題しか起こさないため
    # 一旦 database_exists で存在する場合は drop -> create とするように対処
    # assert not database_exists(
    #     SQLALCHEMY_DB_URL), "Test database already exists. Aborting tests."

    # Create test database and tables
    if database_exists(SQLALCHEMY_DB_URL):
        drop_database(SQLALCHEMY_DB_URL)
        create_database(SQLALCHEMY_DB_URL)
    else:
        create_database(SQLALCHEMY_DB_URL)
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # insert test data
    db = SessionLocal()
    initializeTestData(db)
    db.commit()

    # Run the tests
    yield SessionLocal

    # Drop the test database
    drop_database(SQLALCHEMY_DB_URL)
