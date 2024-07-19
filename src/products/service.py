from uuid import UUID

from products.models import Ingredient, Product, ProductCreate
from sqlmodel import Session, select

# lista de um  produto
# lista dos produtos
# criação dos produtos


def create_product(sesssion: Session, data: ProductCreate):
    products = Product.model_validate(data)
    sesssion.add(products)
    sesssion.commit()
    sesssion.refresh(products)
    for ingredient in data.ingredients:
        ingredient = Ingredient(name=ingredient, id_product=products.id)
        sesssion.add(ingredient)
        sesssion.commit()
        sesssion.refresh(ingredient)

    return products


def list_product(session: Session, id: UUID):
    product = (
        select(Product, Ingredient)
        .join(Ingredient, Ingredient.id_product == Product.id)
        .where(Ingredient.id_product == id)
    )
    ingredients = []
    results = session.exec(product).fetchmany()
    for _, i in results:
        ingredients.append(i.name)

    return ProductCreate(
        name=results[0].Product.name,
        price=results[0].Product.price,
        description=results[0].Product.description,
        img_product=results[0].Product.img_product,
        ingredients=ingredients,
    )
