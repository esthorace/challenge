from app import stock


# {
#     "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
#     "quantity": [3, 10, 0, 5],
# }


def test_stock():
    assert stock.is_product_available("Chocolate", -1) == False
    assert stock.is_product_available("Chocolate", 0) == False
    assert stock.is_product_available("Chocolate", 1) == True
    assert stock.is_product_available("Chocolate", 2) == True
    assert stock.is_product_available("Chocolate", 3) == True
    assert stock.is_product_available("Chocolate", 4) == False
    assert stock.is_product_available("Limon", 0) == False
    assert stock.is_product_available("Dulce de Leche", 5) == True
