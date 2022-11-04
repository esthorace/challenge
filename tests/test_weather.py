from app.weather import GeoAPI


def test_response():
    assert GeoAPI.is_hot_in_pehuajo() in (True, False)
