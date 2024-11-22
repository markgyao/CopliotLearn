# from sqlalchemy import Column, Integer, ForeignKey
# from app.db import Base

# class RolePermission(Base):
#     __tablename__ = "role_permissions"

#     role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True, index=True)
#     permission_id = Column(Integer, ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True, index=True)