from fastapi import FastAPI, HTTPException, APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Dict
from app.models.database import get_db
from ..services.category_services import CategoryService
from ..schemas.category import CategoryCreate, CategoryResponse


router = APIRouter(prefix="domen.com/api/categories", tags=["categories"])

@router.get("",response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_all_categories()


@router.get("/{category_id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def get_category(category_id: int, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_category_by_id(category_id)

