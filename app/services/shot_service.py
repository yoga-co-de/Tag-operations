from fastapi import HTTPException, status
from app.models import models


class ShotService:

    def get_all(db):
        return db.query(models.Shot).filter(
            models.Shot.is_deleted == 0
        ).all()

    def create(db, shot):
        new_shot = models.Shot(
            Studio_id=shot.Studio_id,
            shot_id=shot.shot_id,
            tag_id=shot.tag_id,
            shot_code=shot.shot_code,
            shot_path=shot.shot_path,
            frame_range=shot.frame_range,
            created_by=shot.created_by,
            updated_by=shot.updated_by
        )

        db.add(new_shot)
        db.commit()
        db.refresh(new_shot)
        return new_shot

    def get_by_id(db, id: int):
        shot = db.query(models.Shot).filter(
            models.Shot.id == id,
            models.Shot.is_deleted == 0
        ).first()

        if not shot:
            raise HTTPException(
                status_code=404,
                detail="Shot not found"
            )

        return shot

    def update(db, id: int, shot):
        existing = db.query(models.Shot).filter(
            models.Shot.id == id,
            models.Shot.is_deleted == 0
        ).first()

        if not existing:
            raise HTTPException(
                status_code=404,
                detail="Shot not found"
            )

        update_data = shot.dict(exclude_unset=True)

        db.query(models.Shot).filter(
            models.Shot.id == id
        ).update(update_data)

        db.commit()

        return {"message": "Shot updated successfully"}

    def delete(db, id: int):
        shot = db.query(models.Shot).filter(
            models.Shot.id == id,
            models.Shot.is_deleted == 0
        ).first()

        if not shot:
            raise HTTPException(
                status_code=404,
                detail="Shot not found"
            )

        shot.is_deleted = 1
        db.commit()

        return {"message": "Shot deleted successfully"}



