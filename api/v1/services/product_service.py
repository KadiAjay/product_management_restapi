from api.v1.models.product_model import ProductModel

class ProductService:

    def create_product(self, db, product):
        db_product = ProductModel(
            name=product.name,
            description=product.description,
            price=product.price
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def get_all_products(self, db):
        return db.query(ProductModel).all()

    def get_product_by_id(self, db, product_id):
        return db.query(ProductModel).filter(ProductModel.id == product_id).first()

    def update_product(self, db, product_id, product):
        db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

        if db_product:
            db_product.name = product.name
            db_product.description = product.description
            db_product.price = product.price
            db.commit()
            db.refresh(db_product)

        return db_product

    def delete_product(self, db, product_id):
        db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

        if db_product:
            db.delete(db_product)
            db.commit()

        return {"status": "deleted"}

    def get_product_service():
        return ProductService()