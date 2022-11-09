import logging


_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
                             "heladoFrozen"]


def validate_discount_code(discount_code):
    discount_code_set = {character for character in discount_code}
    for discount_available in _AVAILABLE_DISCOUNT_CODES:
        discount_available_set = {character for character in discount_available}
        symmetric_difference = discount_available_set.symmetric_difference(discount_code_set)
        symmetric_difference_len = len(symmetric_difference)
        if symmetric_difference_len < 3:
            return True
    return False


def input_discount_code() -> bool:
    while True:
        discount_code = input("⚠️ Si tienes un código de descuento, escríbelo: ")
        if validate_discount_code(discount_code):
            print("🎉 Descuento aplicado")
            return True
        else:
            print("⚠️ Lo ingresado no corresponde a un código de descuento")
            r = input("¿Lo vuelves a ingresar? (n: salir):").strip().lower()
            if r == "n":
                return False
            else:
                continue
