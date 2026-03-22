from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.v1.core.db import get_db
from api.v1.services.product_service import ProductService
from api.v1.schema.product_schema import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    service: ProductService = Depends(ProductService.get_product_service)
):
    print("API HIT")
    return service.create_product(db, product)



@router.get("/", response_model=list[ProductResponse])
def get_all_products(
    db: Session = Depends(get_db),
    service: ProductService = Depends(ProductService.get_product_service)
):
    return service.get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    service: ProductService = Depends(ProductService.get_product_service)
):
    return service.get_product_by_id(db, product_id)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db),
    service: ProductService = Depends(ProductService.get_product_service)
):
    return service.update_product(db, product_id, product)


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    service: ProductService = Depends(ProductService.get_product_service)
):
    return service.delete_product(db, product_id)