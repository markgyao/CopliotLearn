# from sqlalchemy import Column, Integer, String, Text, ForeignKey
# from app.db import Base

# class Test(Base):
#     __tablename__ = "tests"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String(255), nullable=False)
#     category_id = Column(Integer, ForeignKey("test_categories.id", ondelete="CASCADE"), nullable=False)
#     description = Column(Text)
#     test_content = Column(Text)
#     test_file_path = Column(String(255))
#     test_answer_file_path = Column(String(255))