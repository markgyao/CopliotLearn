# from sqlalchemy import Column, Integer, ForeignKey, Date, DECIMAL
# from app.db import Base

# class StudentHomework(Base):
#     __tablename__ = "students_homeworks"

#     student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, index=True)
#     homework_id = Column(Integer, ForeignKey("homeworks.id", ondelete="CASCADE"), primary_key=True, index=True)
#     grade = Column(DECIMAL(5, 2), nullable=False)
#     submitted_date = Column(Date, nullable=False)