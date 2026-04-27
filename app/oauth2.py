# from jose import jwt
# from datetime import datetime, timedelta

# SECRET_KEY = "mysecretkey123"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60

# def create_access_token(data: dict):
#     to_encode = data.copy()

#     expire = datetime.utcnow() + timedelta(minutes=60)
#     to_encode.update({"exp": expire})

#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)----->only login and get jwt token

from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import get_db
from app.models import models

SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.user_id == user_id).first()

    if user is None:
        raise credentials_exception

    return user