from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from models import Todos
from database import SessionLocal
import starlette.status as status
from .auth import get_current_user

router = APIRouter(
    prefix = '/admin',
    tags = ['admin']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#* Depends : get_db 함수에 의존한다 -> db 열고 닫기 
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get('/todo',status_code = status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('role') != "admin":
        raise HTTPException(status_code = 401, detail= "Authentication failed")
    return db.query(Todos).all()

