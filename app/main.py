from . import messages, stock, weather, order, discounts


def main():
    """
    1. Solicita a una API por la temperatura de Pehuajó
    2. Si la temperatura es mayor a 28ºC, se da un saludo, si no, se da otro tipo de saludo
    3. Verifica si hay algún producto disponible
    4. Verifica si hay stock en los productos disponibles
    5. Muestra los productos disponibles que tienen stock
    6. El usuario elige un producto y su cantidad
    7. Verifica si hay stock sobre la cantidad del producto solicitada 
    8. El usuario ingresa un código de descuento
    9. Verifica el código de descuento
    10. Confirma el pedido
    """
    while True:
        temperature: bool | None = weather.GeoAPI.is_hot_in_pehuajo()
        if temperature is None:
            messages.no_connection()
            break
        messages.welcome(temperature)

        there_are_products = stock.are_there_products()
        if not there_are_products:
            messages.no_products()
            if messages.query_exit():
                break
            else:
                continue

        products: bool | dict = stock.are_there_stock()
        if isinstance(products, bool):
            messages.no_stock()
            if messages.query_exit():
                break
            else:
                continue

        order_response: bool | tuple[str, int] = order.main(products)
        if isinstance(order_response, bool):
            messages.no_order()
            if messages.query_exit():
                break
            else:
                continue
        product_name, quantity = order_response

        available = stock.is_product_available(product_name, quantity)
        if not available:
            messages.there_are_not_stock()
            if messages.query_exit():
                break
            else:
                continue

        messages.there_are_stock()

        discounts.input_discount_code()
        messages.confirmed_order()
        if messages.query_exit():
            break
        else:
            continue


if __name__ == "__main__":
    main()
