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


def lists_produtos(session: Session):
    # Seleciona produtos e ingredientes e realiza a junção entre eles
    products = select(Product, Ingredient).join(
        Ingredient, Ingredient.id_product == Product.id
    )
    results = session.exec(products).all()

    # Dicionário para armazenar produtos e seus ingredientes
    product_dict = {}

    for product, ingredient in results:
        if product.id not in product_dict:
            # Se o produto não está no dicionário, adicione-o com uma lista vazia de ingredientes
            product_dict[product.id] = {
                "name": product.name,
                "description": product.description,
                "img_product": product.img_product,
                "id": str(product.id),  # Convert UUID to string for serialization
                "price": str(
                    product.price
                ),  # Convert Decimal to string for serialization
                "ingredients": [],
            }
        # Adicione o ingrediente à lista de ingredientes do produto
        product_dict[product.id]["ingredients"].append(
            {"id": ingredient.id, "name": ingredient.name}
        )

    # Converte o dicionário de produtos em uma lista
    product_list = list(product_dict.values())

    return product_list
