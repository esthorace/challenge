from app.discounts import validate_discount_code


def test_validate_discount_code():
    assert validate_discount_code("Primavera2021") == True
    assert validate_discount_code("primavera2021") == True
    assert validate_discount_code("primavera202") == False
    assert validate_discount_code("Verano2021") == True
    assert validate_discount_code("verano2021") == True
    assert validate_discount_code("verano2020") == False
