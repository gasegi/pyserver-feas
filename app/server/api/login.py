import crypt
from hmac import compare_digest
from typing import Optional

from fastapi import Depends, APIRouter, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

# from app.user import crud, models
from database.database import SessionLocal, engine
from sql import staff

router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/api/login")
async def login(
        request: Request,
        response: Response,
        db: Session = Depends(get_db),
        # Optional[str] = None のように書く理由は、Open API(Swagger) で想定通りの粒度で拾ってもらうため
        id: Optional[str] = None,
        password: Optional[str] = None
):
    salt = "random value"  # システム全体で共有、あるいはユーザーごとに可変が望ましい

    print("crypt.crypt", crypt.crypt(password, salt))  # for debug
    print(id)
    print(password)
    # crypt.crypt user1=raM7IbozF4Awk
    # crypt.crypt usertest=raFF41zUzpYwU

    result = db.execute(staff.login_sql.format(id))
    db.commit()

    success_flag = False

    for row in result:
        print("staff_name:", row['staff_name'])
        print("password:", row['password'])

        if compare_digest(crypt.crypt(password, salt), row['password']):
            success_flag = True

    if success_flag:
        # response.status_code = status.HTTP_201_CREATED
        return True
    else:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password")
