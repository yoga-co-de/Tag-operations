from fastapi import HTTPException, status
from app.models import models


class StudioService:

    def get_all(db):
        return db.query(models.Studio).all()

    def create(db, studio):
        new_studio = models.Studio(
            studio_name=studio.studio_name
        )

        db.add(new_studio)
        db.commit()
        db.refresh(new_studio)
        return new_studio

    def get_by_id(db, studio_id: int):
        studio = db.query(models.Studio).filter(models.Studio.studio_id == studio_id).first()

        if not studio:
            raise HTTPException(
                status_code=404,
                detail="Studio not found"
            )
        return studio

    def update(db, studio_id: int, studio):
        existing = db.query(models.Studio).filter(models.Studio.studio_id == studio_id).first()

        if not existing:
            raise HTTPException(status_code=404, detail="Studio not found")

        update_data = studio.dict(exclude_unset=True)

        db.query(models.Studio).filter(models.Studio.studio_id == studio_id).update(update_data)
        db.commit()

        return {"message": "Studio updated successfully"}

    def delete(db, studio_id: int):
        studio = db.query(models.Studio).filter(models.Studio.studio_id == studio_id).first()

        if not studio:
            raise HTTPException(status_code=404, detail="Studio not found")

        db.delete(studio)
        db.commit()

        return {"message": "Studio deleted successfully"}