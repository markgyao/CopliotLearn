# from sqlalchemy import Column, Integer, String
# from app.db import Base

# class Permission(Base):
#     __tablename__ = "permissions"

#     id = Column(Integer, primary_key=True, index=True)
#     permission_name = Column(String(255), unique=True, index=True, nullable=False)
#     description = Column(String(255))
#     resource = Column(String(255), nullable=False)
#     action = Column(String(50), nullable=False)