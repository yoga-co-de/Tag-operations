from fastapi import FastAPI, Response, status, HTTPException, Depends
from database import engine,Base,get_db
from app.models import models
from sqlalchemy.orm import Session





def get_tags_by_user(db: Session, user_id: int):
        user = db.query(models.User).filter(models.User.user_id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        studio_id = user.studio_id
        tags = db.query(models.Tag).filter(models.Tag.studio_id == studio_id).all()

        return tags
    
    
    


def create(db, tag):            
        studio = db.query(models.Studio).filter(models.Studio.studio_id == tag.studio_id).first()
        if not studio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Studio with id {tag.studio_id} not found"
            )            
        user = db.query(models.User).filter(models.User.user_id == tag.user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {tag.user_id} not found"
            )
        new_tag = models.Tag(studio_id=tag.studio_id,tag_name=tag.tag_name,description=tag.description,
            is_deleted=False,updated_by=user.user_id)
        db.add(new_tag)
        db.commit()
        db.refresh(new_tag)
        return new_tag
    

def get_id(db, user_id, tag_id):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(404, "Tag not found")
    if tag.studio_id != user.studio_id:
        raise HTTPException(403, "Not allowed")
    return tag



def update(db, user_id, tag_id, tag_data):

    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")

    tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(404, "Tag not found")

    if tag.studio_id != user.studio_id:
        raise HTTPException(403, "Not allowed")

    
    allowed_fields = {"tag_name", "description"}

    for key, value in tag_data.dict(exclude_unset=True).items():
        if key in allowed_fields:
            setattr(tag, key, value)

    
    tag.updated_by = user.user_id

    db.commit()
    db.refresh(tag)
    return tag
def delete(db, user_id, tag_id):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(404, "Tag not found")
    if tag.studio_id != user.studio_id:
        raise HTTPException(403, "Not allowed")

    tag.is_delete = 1
    db.commit()
    return {"message": "Tag deleted"}
