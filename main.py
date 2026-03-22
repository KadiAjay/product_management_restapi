from fastapi import FastAPI
from api.v1.routes import product_routes
from api.v1.core.db import engine
from api.v1.models.product_model import ProductModel

ProductModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_routes.router, prefix="/api/v1")