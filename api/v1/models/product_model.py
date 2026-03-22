from sqlalchemy import Column, Integer, String, Float
from api.v1.core.db import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    #this file is for createing table