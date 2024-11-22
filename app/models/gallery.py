from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from app.db import Base

class Gallery(Base):
    __tablename__ = "gallery"

    image_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    image_path = Column(String(255), nullable=False)
    description = Column(Text)
    upload_date = Column(Date, nullable=False)
    image_title = Column(String(100))