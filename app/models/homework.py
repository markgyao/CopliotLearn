# from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
# from app.db import Base

# class Homework(Base):
#     __tablename__ = "homeworks"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(255), nullable=False)
#     class_id = Column(Integer, ForeignKey("classes.id", ondelete="CASCADE"), nullable=False)
#     description = Column(Text)
#     homework_content = Column(Text)
#     due_date = Column(Date)
#     file_path = Column(String(255))
#     answer_key_path = Column(String(255))
#     grade_level = Column(String(20))