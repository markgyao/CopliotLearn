from sqlalchemy import Column, Integer, String
from app.db import Base

class TestCategory(Base):
    __tablename__ = "test_categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    level = Column(String(255))