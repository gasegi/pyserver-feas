from starlette.testclient import TestClient
# from fastapi import Depends
from sqlalchemy.orm import Session

from main import app
from test.common import temp_db
from database.database import SessionLocal, get_db
from sql.staff import Staff

client = TestClient(app)


@temp_db
def test_login_success(session: SessionLocal):

    # 基本のテスト
    response = client.get("/api/login?id=user1&password=usertest")
    assert response.json() == True
    assert response.status_code == 200

    # 各テストでデータベースにデータを追加したい時
    db = session()
    objects = [
        Staff(staff_number='user2test', staff_name='鈴木テスト2',
              password='raFF41zUzpYwU', admin_flag=0, delete_flag=0)
    ]
    db.bulk_save_objects(objects)
    db.commit()

    response = client.get("/api/login?id=user2test&password=usertest2")
    assert response.json() == True
    assert response.status_code == 200

    # response = client.post(
    #     "/users/", json={"email": "foo", "password": "fo"}
    # )


@temp_db
def test_login_success2(session: SessionLocal):

    # 基本のテスト
    # response = client.get("/api/login?id=user1&password=usertest")
    # assert response.json() == True
    # assert response.status_code == 200

    # 各テストでデータベースにデータを追加したい時
    # db = session()
    # objects = [
    #     Staff(staff_number='user2test', staff_name='鈴木テスト2',
    #           password='raFF41zUzpYwU', admin_flag=0, delete_flag=0)
    # ]
    # db.bulk_save_objects(objects)
    # db.commit()

    response = client.get("/api/login?id=user1&password=usertest")
    assert response.json() == True
    assert response.status_code == 200

    # response = client.post(
    #     "/users/", json={"email": "foo", "password": "fo"}
    # )
