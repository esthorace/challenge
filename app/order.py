import logging


def show_products(products: dict) -> None:
    print("\nProductos y stock disponible:")
    for index, product_quantity in products.items():
        print(f" {index} - {product_quantity[0]} (cantidad: {product_quantity[1]})")
    print(" S - Salir")
    print()


def choose_product(products: dict) -> str | bool:
    while True:
        product = input("Elija el producto: ")
        if product.strip().lower() == "s":
            return False
        if product.strip().lower() not in products:
            print("Vuelva a intentar elegir el producto")
        else:
            product_name = products[product][0]
            return product_name


def choose_quantity() -> int | bool:
    while True:
        quantity = input("Escriba la cantidad: ")
        if quantity.strip().lower() == "s":
            return False
        try:
            quantity_int = int(quantity)
        except ValueError:
            print("La cantidad debe ser un número entero")
        except KeyboardInterrupt:
            return False
        else:
            if quantity_int < 0 or quantity_int == 0:
                print("La cantidad debe se mayor a 0")
            else:
                return quantity_int


def main(products) -> bool | tuple:
    while True:
        show_products(products)
        product_name = choose_product(products)
        if not product_name:
            return False
        quantity = choose_quantity()
        if not quantity:
            continue
        return product_name, quantity
