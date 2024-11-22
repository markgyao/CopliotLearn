# from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
# from app.db import Base

# class Class(Base):
#     __tablename__ = "classes"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(255), nullable=False)
#     teacher_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
#     starting_date = Column(Date, nullable=False)
#     ending_date = Column(Date, nullable=False)
#     descriptions = Column(Text)
#     subject = Column(String(255), nullable=False)