from pydantic import BaseModel
from typing import Optional
from datetime import date

class GalleryBase(BaseModel):
    student_id: int
    image_path: str
    description: Optional[str] = None
    upload_date: date
    image_title: Optional[str] = None

class GalleryCreate(GalleryBase):
    pass

class Gallery(GalleryBase):
    image_id: int

    class Config:
        orm_mode = True