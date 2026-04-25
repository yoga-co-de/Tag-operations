from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas import user_schema
from app.services.user_service import UserService

api = APIRouter(prefix="/users", tags=["Users"])


@api.get("/")
def get_users(db: Session = Depends(get_db)):
    return UserService.get_all(db)


@api.post("/", status_code=status.HTTP_201_CREATED, response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return UserService.create(db, user)


@api.get("/{user_id}", response_model=user_schema.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_by_id(db, user_id)


@api.put("/{user_id}")
def update_user(user_id: int, user: user_schema.UserUpdate, db: Session = Depends(get_db)):
    return UserService.update(db, user_id, user)


@api.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete(db, user_id)