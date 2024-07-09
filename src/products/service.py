from products.models import Product
from sqlmodel import Session, select


def create_product(sesssion: Session, data: Product):
    products = Product.model_validate(data)

    sesssion.add(products)
    sesssion.commit()
    sesssion.refresh(products)
    return products


def list_product(session: Session, id: int):
    product = select(Product).where(Product.id == id)
    results = session.exec(product).first()
    return results
