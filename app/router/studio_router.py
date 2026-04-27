from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas import studio_schema
from app.services.studio_service import StudioService
from app import oauth2

api = APIRouter(prefix="/studios", tags=["Studios"])


@api.get("/")
def get_studios(db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    return StudioService.get_all(db)


@api.post("/", status_code=status.HTTP_201_CREATED, response_model=studio_schema.StudioResponse)
def create_studio(studio: studio_schema.StudioCreate, db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    return StudioService.create(db, studio)


@api.get("/{studio_id}", response_model=studio_schema.StudioResponse)
def get_studio(studio_id: int, db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    return StudioService.get_by_id(db, studio_id)


@api.put("/{studio_id}")
def update_studio(studio_id: int, studio:studio_schema.StudioUpdate, db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    return StudioService.update(db, studio_id, studio)


@api.delete("/{studio_id}")
def delete_studio(studio_id: int, db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    return StudioService.delete(db, studio_id)