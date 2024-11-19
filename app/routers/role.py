from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import role as crud_role
from app.schemas import role as schema_role
from app.db import get_db

router = APIRouter()

@router.post("/roles/", response_model=schema_role.Role)
def create_role(role: schema_role.RoleCreate, db: Session = Depends(get_db)):
    return crud_role.create_role(db, role)

@router.get("/roles", response_model=list[schema_role.Role])
def get_all_roles(db: Session = Depends(get_db)):
    return crud_role.get_all_roles(db)

@router.get("/roles/{role_id}", response_model=schema_role.Role)
def get_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud_role.get_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    return crud_role.delete_role(db, role_id)