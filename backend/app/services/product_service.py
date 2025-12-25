from sqlalchemy.orm import Session
from typing import List, Optional
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductResponse
from fastapi import HTTPException, status
from app.repositories.category_repository import CategoryRepository

class ProductService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)