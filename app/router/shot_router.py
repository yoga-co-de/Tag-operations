from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas import shot_Schema
from app.services.shot_service import ShotService
from app import oauth2

api = APIRouter(prefix="/shots", tags=["Shots"])


@api.get("/")
def get_shots(
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    return ShotService.get_all(db)


@api.post("/", status_code=status.HTTP_201_CREATED, response_model=shot_Schema.ShotResponse)
def create_shot(
    shot: shot_Schema.ShotCreate,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    return ShotService.create(db, shot)


@api.get("/{id}", response_model=shot_Schema.ShotResponse)
def get_shot(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    return ShotService.get_by_id(db, id)


@api.put("/{id}")
def update_shot(
    id: int,
    shot: shot_Schema.ShotUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    return ShotService.update(db, id, shot)


@api.delete("/{id}")
def delete_shot(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    return ShotService.delete(db, id)