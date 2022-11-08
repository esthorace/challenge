def show_message(message) -> None:
    print(message)


def query_exit() -> bool:
    r = input("¿Quieres salir ('s') o continuar <enter>?: ")
    if r.upper().strip() == "S":
        return True
    else:
        return False


def no_connection() -> None:
    message = "❌ No tenemos conexión por el momento. Vuelve a intentar."
    show_message(message)


def welcome(temperature) -> None:
    if temperature:  # Mayor a 28 grados
        message = "👋 ¡Bienvenido! Hoy hace calor, un buen helado puede refrescarte..."
    else:
        message = "👋 ¡Bienvenido! Hoy está fresco, y, aún así, algo dulce puede venirte bien..."
    show_message(message)


def no_products() -> None:
    message = "⚠️ No hay productos para solicitar"
    show_message(message)


def no_stock() -> None:
    message = "⚠️ No hay stock, no se puede solicitar productos"
    show_message(message)


def no_order() -> None:
    message = "⚠️ No hay pedido de productos"
    show_message(message)


def there_are_stock() -> None:
    message = "***** 😊 Hay stock del producto seleccionado"
    show_message(message)


def there_are_not_stock() -> None:
    message = "***** 😔 No hay stock del producto seleccionado"
    show_message(message)
