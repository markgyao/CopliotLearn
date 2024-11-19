from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    grade_level = Column(String(255), nullable=False)
    main_parent_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    secondary_parent_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    addional_info = Column(Text)
    food_allergy = Column(Text)