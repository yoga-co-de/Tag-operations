# from fastapi import APIRouter, Depends, status,HTTPException
# from sqlalchemy.orm import Session
# from database import get_db
# from app.schemas import user_schema
# from app.services.user_service import UserService
# from app import oauth2,utils
# from app.models import models
# api = APIRouter(prefix="/users", tags=["Users"])


# @api.get("/")
# def get_users(db: Session = Depends(get_db)):
#     return UserService.get_all(db)


# @api.post("/", status_code=status.HTTP_201_CREATED, response_model=user_schema.UserResponse)
# def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
#     return UserService.create(db, user)


# @api.post("/login", response_model=user_schema.Token)
# def login(user_credentials: user_schema.UserLogin, db: Session = Depends(get_db)):

#     user = db.query(models.User).filter(
#         models.User.email == user_credentials.email
#     ).first()

#     if not user:
#         raise HTTPException(status_code=403, detail="Invalid Credentials")

#     if not utils.verify(user_credentials.password, user.password):
#         raise HTTPException(status_code=403, detail="Invalid Credentials")

#     access_token = oauth2.create_access_token(
#         data={"user_id": user.user_id}
#     )

#     return {
#         "access_token": access_token,
#         "token_type": "bearer"
#     }




# @api.get("/{user_id}", response_model=user_schema.UserResponse)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     return UserService.get_by_id(db, user_id)


# @api.put("/{user_id}")
# def update_user(user_id: int, user: user_schema.UserUpdate, db: Session = Depends(get_db)):
#     return UserService.update(db, user_id, user)


# @api.delete("/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     return UserService.delete(db, user_id)


from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from app.schemas import user_schema
from app.services.user_service import UserService
from app.models import models
from app import utils, oauth2
from fastapi.security import OAuth2PasswordRequestForm

api = APIRouter(prefix="/users", tags=["Users"])


# PUBLIC
@api.post("/", status_code=status.HTTP_201_CREATED, response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return UserService.create(db, user)


# PUBLIC LOGIN
# @api.post("/login", response_model=user_schema.Token)
# def login(user_credentials: user_schema.UserLogin, db: Session = Depends(get_db)):

#     user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

#     if not user:
#         raise HTTPException(status_code=403, detail="Invalid Credentials")

#     if not utils.verify(user_credentials.password, user.password):
#         raise HTTPException(status_code=403, detail="Invalid Credentials")

#     access_token = oauth2.create_access_token(
#         data={"user_id": user.user_id}
#     )

#     return {
#         "access_token": access_token,
#         "token_type": "bearer"
#     }
@api.post("/login", response_model=user_schema.Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.email == user_credentials.username
    ).first()

    if not user:
        raise HTTPException(status_code=403, detail="Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=403, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(
        data={"user_id": user.user_id}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


#  PROTECTED
@api.get("/")
def get_users(
    db: Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    return UserService.get_all(db)


@api.get("/{user_id}")
def get_user(user_id: int,db: Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    return UserService.get_by_id(db, user_id)


@api.put("/{user_id}")
def update_user(user_id: int,user: user_schema.UserUpdate,db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):
    return UserService.update(db, user_id, user)


@api.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):
    return UserService.delete(db, user_id)