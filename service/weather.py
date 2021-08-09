import requests
from bs4 import BeautifulSoup


WEATHER_API_BASE_URL = 'https://www.alojz.cz'


class WeatherApiError(RuntimeError):
    """Means that weather API could not be reached or contains no data."""


def get_weather_info(city: str) -> str:
    response = requests.get(f'{WEATHER_API_BASE_URL}/{city}')
    if response.status_code != 200:
        raise WeatherApiError
    soup = BeautifulSoup(response.content, "html.parser")
    item = soup.select_one(
        "body > div.wrapper > section > article:nth-child(1) > h2.actual-forecast")
    if item == None:
        raise WeatherApiError
    return str(item.contents).replace("\\n", "").strip("[]").strip("' ")
