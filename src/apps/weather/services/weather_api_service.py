import logging
from decimal import Decimal
from typing import List, Optional, Dict
from urllib.parse import urlencode

import requests
from apps.weather.dto import LocationDTO
from apps.weather.exceptions import WeatherApiException
from apps.weather.services.location_service import LocationService
from config import settings

logger = logging.getLogger('weather.services.weather_api_service')


class WeatherApiService:
    @classmethod
    def handle_exceptions(cls, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"api.openweathermap.org - Error {response.json()}")
            raise WeatherApiException

    @classmethod
    def get_location(cls, location):
        """Получает список городов."""
        params = {
            "q": location,
            "limit": 5,
            "appid": settings.WEATHER_API_KEY,
        }
        url = f'http://api.openweathermap.org/geo/1.0/direct?{urlencode(params)}'

        return cls.handle_exceptions(url)

    @classmethod
    def get_forecast(cls, latitude: Decimal, longitude: Decimal) -> Optional[Dict]:
        """Получает прогноз погоды по координатам (широта и долгота)."""
        params = {
            "lat": latitude,
            "lon": longitude,
            "lang": "ru",
            "appid": settings.WEATHER_API_KEY,
            "units": "metric",
        }
        url = f"https://api.openweathermap.org/data/2.5/weather?{urlencode(params)}"

        return cls.handle_exceptions(url)

    @classmethod
    def location_forecast_dto(cls, user_id: int) -> List[LocationDTO]:
        dto_list = []
        queryset = LocationService.get_all_locations(user_id)
        for query in queryset:
            dto_list.append(
                LocationDTO(
                    name_city=query.name,
                    latitude=query.latitude,
                    longitude=query.longitude,
                    weather=cls.get_forecast(query.latitude, query.longitude)
                ))
        return dto_list
