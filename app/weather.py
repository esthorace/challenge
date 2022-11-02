import requests


class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?lat={cls.LAT}"
            f"&lon={cls.LON}"
            f"&units=metric"
            f"&appid={cls.API_KEY}"
        )
        if response.status_code == 200:
            response_dict = response.json()
            temperature = float(response_dict["main"]["temp"])
            if temperature > 28:
                return True
            else:
                return False
        else:
            return False
