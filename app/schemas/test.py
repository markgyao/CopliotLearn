from pydantic import BaseModel
from typing import Optional

class TestBase(BaseModel):
    name: str
    category_id: int
    description: Optional[str] = None
    test_content: Optional[str] = None
    test_file_path: Optional[str] = None
    test_answer_file_path: Optional[str] = None

class TestCreate(TestBase):
    pass

class Test(TestBase):
    id: int

    class Config:
        orm_mode = True