from products.models import Product
from sqlmodel import Session


def create_product(sesssion: Session, data: Product):
    products = Product.model_validate(data)

    sesssion.add(products)
    sesssion.commit()
    sesssion.refresh(products)
    return products
