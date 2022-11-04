import pandas as pd
import logging


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

_PRODUCT_DF = pd.DataFrame(
    {
        "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
        "quantity": [3, 10, 0, 5],
    }
)


def is_product_available(product_name: str, quantity: int):

    # Validate product name
    if not isinstance(product_name, str):
        logging.error("Value is not str")
        return False

    # Validate quantity
    if not isinstance(quantity, int):
        logging.error("Value is not int")
        return False
    elif quantity < 0:
        logging.warning("Value is less than 0")
        return False
    elif quantity == 0:
        logging.warning("Value is equal to 0")
        return False

    # Get product name
    product: pd.DataFrame = _PRODUCT_DF[_PRODUCT_DF["product_name"] == product_name]
    if product.empty:
        logging.warning(f"Value '{product_name}' not found")
        return False

    # Function
    stock: bool = (product["quantity"] > quantity).bool()
    if stock:
        logging.info("Stock is available")
        return True
    else:
        logging.info("Stock is not available")
        return False
