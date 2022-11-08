from . import messages, stock, weather, order


def main():
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
        if available:
            messages.there_are_stock()
        else:
            messages.there_are_not_stock()

        if messages.query_exit():
            break
        else:
            continue


if __name__ == "__main__":
    main()
