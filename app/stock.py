import pandas as pd
import logging


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

_PRODUCT_DF = pd.DataFrame(
    {
        "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
        "quantity": [3, 10, 0, 5],
    }
)


def are_there_products() -> bool:
    """Verifica si existen productos en los datos, por lo menos uno"""
    logging.debug("Verificando productos")
    if len(_PRODUCT_DF):
        return True
    else:
        return False


def are_there_stock() -> bool | dict:
    """Verifica en todos los productos si hay, aunque sea en uno, stock"""
    logging.debug("Verificando stock en productos")
    products = _PRODUCT_DF.query("quantity > 0")
    if products.empty:
        return False
    else:
        products_dict = {}
        products_list = products.to_numpy().tolist()
        for index, product in enumerate(products_list, start=1):
            products_dict[str(index)] = product
        return products_dict


def is_product_available(product_name: str, quantity: int) -> bool:
    """Verifica si hay stock según la cantidad especificada para el producto especificado"""
    logging.debug("Verificando si hay stock en el producto seleccionado")
    if not isinstance(quantity, int) or quantity <= 0:
        return False
    product: pd.DataFrame = _PRODUCT_DF[_PRODUCT_DF["product_name"] == product_name]
    stock: bool = (product["quantity"] >= quantity).bool()
    if stock:
        return True
    else:
        return False
