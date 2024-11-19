from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import gallery as crud_gallery
from app.schemas import gallery as schema_gallery
from app.db import get_db

router = APIRouter()

@router.post("/gallery/", response_model=schema_gallery.Gallery)
def create_gallery(gallery: schema_gallery.GalleryCreate, db: Session = Depends(get_db)):
    return crud_gallery.create_gallery(db, gallery)

@router.get("/gallery", response_model=list[schema_gallery.Gallery])
def get_all_galleries(db: Session = Depends(get_db)):
    return crud_gallery.get_all_galleries(db)

@router.get("/gallery/{image_id}", response_model=schema_gallery.Gallery)
def get_gallery(image_id: int, db: Session = Depends(get_db)):
    db_gallery = crud_gallery.get_gallery(db, image_id)
    if db_gallery is None:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return db_gallery

@router.delete("/gallery/{image_id}")
def delete_gallery(image_id: int, db: Session = Depends(get_db)):
    return crud_gallery.delete_gallery(db, image_id)