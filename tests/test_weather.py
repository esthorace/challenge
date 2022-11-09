from app.weather import GeoAPI


def test_response():
    """La conexión o es True o False"""
    assert GeoAPI.is_hot_in_pehuajo() in (True, False)
