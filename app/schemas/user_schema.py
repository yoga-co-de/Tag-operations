from pydantic import BaseModel,EmailStr,Field
from typing import Optional



class UserCreate(BaseModel):

    first_name: Optional[str] = None
    last_name: str
    email: Optional[EmailStr] = None#Optional[Emailstr] 
    password :str=Field(..., min_length=6, max_length=72)
    studio_id : int



class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None#Optional[Emailstr] 
    is_active: Optional[int] = None
    is_delete: Optional[int] = None

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    user_id: int
    first_name: Optional[str]
    last_name: str
    email:Optional[EmailStr] 
    is_active: Optional[int]
    is_delete: Optional[int]

    class Config:
        from_attributes = True