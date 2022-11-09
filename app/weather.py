import logging

import requests


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)


class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    TEMPERATURE: int = 28

    @classmethod
    def is_hot_in_pehuajo(cls) -> bool | None:
        """Comprueba la temperatura en tiempo real usando una API. 
        Devuelve True si es mayor a la temperature dada, o False."""
        try:
            logging.debug("Abriendo API")
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?lat={cls.LAT}"
                f"&lon={cls.LON}"
                f"&units=metric"
                f"&appid={cls.API_KEY}"
            )
        except requests.exceptions.RequestException:
            logging.error("Error de conexión")
            return None
        else:
            if response.status_code == 200:
                response_dict = response.json()
                temperature = float(response_dict["main"]["temp"])
                if temperature > cls.TEMPERATURE:
                    logging.info(f"La temperatura es mayor a la estimada: {temperature}º")
                    return True
                else:
                    logging.info(f"La temperatura es menor a la estimada: {temperature}º")
                    return False
            else:
                logging.warning("La respuesta de OpenWeatherMap no está disponible")
                return False
