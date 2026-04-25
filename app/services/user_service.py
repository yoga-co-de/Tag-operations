from fastapi import HTTPException, status
from app.models import models
from app import utils





class UserService:

    def get_all(db):
        return db.query(models.User).all()

    def create(db, user):

        hashed_password=utils.hash(user.password)
        user.password=hashed_password


        new_user = models.User(
            studio_id=user.studio_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password = hashed_password,
            is_active=1,
            is_delete=0
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_by_id(db, user_id: int):
        user = db.query(models.User).filter(models.User.user_id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {user_id} not found"
            )
        return user

    def update(db, user_id: int, user):
        existing = db.query(models.User).filter(models.User.user_id == user_id).first()

        if not existing:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        update_data = user.dict(exclude_unset=True)
        db.query(models.User).filter(models.User.user_id == user_id).update(update_data)

        db.commit()
        return {"message": "User updated successfully"}

    def delete(db, user_id: int):
        user = db.query(models.User).filter(models.User.user_id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        user.is_delete = 1
        db.commit()

        return {"message": "User soft deleted successfully"}
    
    