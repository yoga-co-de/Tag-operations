from fastapi import status,Depends ,APIRouter,HTTPException
#from pydantic import BaseModel
#import time
from app.models import models
from database import engine,Base,get_db
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.services import tag_service
from app import oauth2




#app = FastAPI()
api=APIRouter(
    prefix="/tags",
    tags=["tag_routs"]
)


models.Base.metadata.create_all(bind=engine)

@api.get("/get_tag/by-user/{user_id}")
def get_tags_by_user(user_id: int, db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):

    post=tag_service.get_tags_by_user(db,user_id)
    return post

# create a tag

@api.post("/create_tag",status_code=status.HTTP_201_CREATED,response_model=schemas.Tag_R)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    new_tag=tag_service.create(db,tag)
    return new_tag

#get by tagid,user_id
@api.get("/tags/{tag_id}", response_model=schemas.TagResponse)
def get_tag(tag_id: int,user_id: int,db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    return tag_service.get_id(db, user_id, tag_id)

# update with id

@api.put("/tags/{tag_id}")
def update_tag(tag_id: int,user_id: int,tag: schemas.TagUpdate,db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    return tag_service.update(db, user_id, tag_id, tag)

#id_delete
@api.delete("/tags/{tag_id}")
def delete_tag(tag_id: int,user_id: int,db: Session = Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    return tag_service.delete(db, user_id, tag_id)