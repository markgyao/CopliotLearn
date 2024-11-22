# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.crud import class_crud as crud_class
# from app.schemas import class_schemas as schema_class
# from app.db import get_db

# router = APIRouter()

# # Create a new class
# @router.post("/classes/", response_model=schema_class.Class)
# def create_class(class_: schema_class.ClassCreate, db: Session = Depends(get_db)):
#     return crud_class.create_class(db, class_)

# # Get all classes
# @router.get("/classes", response_model=list[schema_class.Class])
# def get_all_classes(db: Session = Depends(get_db)):
#     return crud_class.get_all_classes(db)

# # Get a specific class by class_id
# @router.get("/classes/{class_id}", response_model=schema_class.Class)
# def get_class(class_id: int, db: Session = Depends(get_db)):
#     db_class = crud_class.get_class(db, class_id)
#     if db_class is None:
#         raise HTTPException(status_code=404, detail="Class not found")
#     return db_class

# # Delete a specific class by class_id
# @router.delete("/classes/{class_id}")
# def delete_class(class_id: int, db: Session = Depends(get_db)):
#     return crud_class.delete_class(db, class_id)