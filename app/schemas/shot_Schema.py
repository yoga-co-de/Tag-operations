from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ShotBase(BaseModel):
    Studio_id: int
    shot_id: int
    tag_id: int
    shot_code: int
    shot_path: str
    frame_range: int


class ShotCreate(ShotBase):
    created_by: int
    updated_by: int


class ShotUpdate(BaseModel):
    Studio_id: Optional[int] = None
    shot_id: Optional[int] = None
    tag_id: Optional[int] = None
    shot_code: Optional[int] = None
    shot_path: Optional[str] = None
    frame_range: Optional[int] = None
    updated_by: Optional[int] = None

    class Config:
        from_attributes = True


class ShotResponse(ShotBase):
    id: int
    is_deleted: int
    created_by: int
    created_date: datetime
    updated_by: int
    updated_date: datetime
    last_updated_date: datetime

    class Config:
        from_attributes = True


class MessageResponse(BaseModel):
    message: str