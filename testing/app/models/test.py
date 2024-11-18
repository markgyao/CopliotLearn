from pydantic import BaseModel

class TestCategoryBase(BaseModel):
    name: str
    subject: str
    level: str | None = None

class TestCategoryCreate(TestCategoryBase):
    pass

class TestCategory(TestCategoryBase):
    id: int

    class Config:
        orm_mode = True