from pydantic import BaseModel
from typing import Optional

class TestCategoryBase(BaseModel):
    name: str
    subject: str
    level: Optional[str] = None

class TestCategoryCreate(TestCategoryBase):
    pass

class TestCategory(TestCategoryBase):
    id: int

    class Config:
        orm_mode = True