from uuid import UUID

from products.models import Product
from sqlmodel import Session, select

# lista do produto
# lista dos produtos
# criação dos produtos


def create_product(sesssion: Session, data: Product):
    products = Product.model_validate(data)

    sesssion.add(products)
    sesssion.commit()
    sesssion.refresh(products)
    return products


def list_product(session: Session, id: UUID):
    product = select(Product).where(
        Product.id == id
    )  # busca pelo id do produto, que foi passa pelo link /{id}
    results = session.exec(product).first()
    return results
