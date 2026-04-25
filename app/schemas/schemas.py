from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Tag(BaseModel):
    studio_id : int
    tag_name : str
    description: Optional[str] = None

class Tag_R(BaseModel):
    id:int
    studio_id : int
    tag_name : str
    description: Optional[str] = None


class TagCreate(BaseModel):
    tag_name : str 
    description: Optional[str] = None
    studio_id : int
    user_id : int
   # is_deleted : bool=False

class TagUpdate(BaseModel):
    tag_name: Optional[str] = None
    description: Optional[str] = None
    # user_id : Optional[int]= None
    # studio_id : Optional[int]=None
    class Config:
        from_attributes = True 

class TagResponse(Tag):

    studio_id : int
    tag_name : str
    description: str
    updated_by: int
    updated_date: datetime

    class config:
        from_attributes =True


    

class MessageResponse(BaseModel):
    message: str
