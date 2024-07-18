from typing import Dict, List

import requests
from django.conf import settings
from requests import Response
from requests.exceptions import ConnectionError, InvalidHeader

BASE_URL: str = settings.BASE_URL
API_KEY: str = settings.API_KEY
API_WEATHER_BASE_URL: str = settings.API_WEATHER_BASE_URL


def get_data(url: str, headers: Dict) -> Response:
    try:
        return requests.get(url, headers=headers)
    except (ConnectionError, InvalidHeader):
        response = Response()
        response.status_code = 400
        return response


def find_city_by_name(name: str) -> Dict:
    api_url: str = f"{BASE_URL}{name}"
    response = get_data(api_url, {"X-Api-Key": API_KEY})
    status = True if response.status_code == 200 else False

    if status:
        return {"status": status, "result": response.json()}
    else:
        return {"status": status}


def get_city_data(name: str) -> Dict:
    api_url: str = f"{BASE_URL}{name}"
    response = get_data(api_url, headers={"X-Api-Key": API_KEY})
    status = True if response.status_code == 200 else False

    if status:
        result = (
            [i for i in response.json() if i.get("name") == name][0]
            if len(response.json())
            else {}
        )
        return {"status": status, "result": result}
    else:
        return {"status": status}


def get_city_names(name: str) -> List[str]:
    data: Dict = find_city_by_name(name)
    return [i.get("name") for i in data.get("result")] if data.get("status") else []


def get_weather_by_geo_data(lat: float, lon: float) -> Dict:
    api_url: str = (
        f"{API_WEATHER_BASE_URL}?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
    )
    response = get_data(api_url, {})

    status = True if response.status_code == 200 else False

    if status:
        temperature = response.json().get("current").get("temperature_2m")
        wind_speed = response.json().get("current").get("wind_speed_10m")
        return {
            "status": status,
            "result": {"temperature": temperature, "wind_speed": wind_speed},
        }
    else:
        return {"status": status}
