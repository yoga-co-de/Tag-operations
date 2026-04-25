from pydantic import BaseModel
from typing import Optional


class StudioCreate(BaseModel):
    studio_name: str


class StudioUpdate(BaseModel):
    studio_name: Optional[str] = None

    class Config:
        from_attributes = True


class StudioResponse(BaseModel):
    studio_id: int
    studio_name: str

    class Config:
        from_attributes = True



