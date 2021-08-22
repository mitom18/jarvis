import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


WEATHER_API_BASE_URL = 'https://www.alojz.cz'


class WeatherApiError(RuntimeError):
    """Means that weather API could not be reached or contains no data."""


@dataclass
class WeatherInfo:
    """Class representing weather API response."""
    place_and_date: str
    info: str


def get_weather_info(city: str) -> WeatherInfo:
    response = requests.get(f'{WEATHER_API_BASE_URL}/{city}')
    if response.status_code != 200:
        raise WeatherApiError
    soup = BeautifulSoup(response.content, "html.parser")
    place_and_date = soup.select_one(
        "body > div.wrapper > section > article:nth-child(1) > p.place-and-date")
    info = soup.select_one(
        "body > div.wrapper > section > article:nth-child(1) > h2.actual-forecast")
    if place_and_date == None or info == None:
        raise WeatherApiError
    place_and_date = str(place_and_date.contents).replace(
        "\\n", "").strip("[]").strip("' ").replace(":", "")
    return WeatherInfo(
        place_and_date=first_upper(place_and_date),
        info=str(info.contents).replace("\\n", "").strip("[]").strip("' ")
    )


def first_upper(string: str) -> str:
    return string[0].upper() + string[1:]
