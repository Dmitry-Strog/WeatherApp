import json
from decimal import Decimal
from typing import List, Optional, Dict
from urllib.parse import urlencode

import requests
from django.db.models import QuerySet

from apps.weather.dto import LocationDTO
from apps.weather.services.location_service import LocationService
from config import settings


class WeatherApiService:
    @staticmethod
    def get_cities(city):
        """Получает список городов."""
        params = {
            "q": city,
            "limit": 5,
            "appid": settings.WEATHER_API_KEY,
        }
        url = f'http://api.openweathermap.org/geo/1.0/direct?{urlencode(params)}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

    @staticmethod
    def get_forecast(latitude: Decimal, longitude: Decimal) -> Optional[Dict]:
        """Получает прогноз погоды по координатам (широта и долгота)."""
        params = {
            "lat": latitude,
            "lon": longitude,
            "lang": "ru",
            "appid": settings.WEATHER_API_KEY,
            "units": "metric",
        }
        url = f"https://api.openweathermap.org/data/2.5/weather?{urlencode(params)}"

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

    def location_forecast_dto(self, user_id: int) -> List[LocationDTO]:
        dto_list = []
        queryset = LocationService.get_all_locations(user_id)
        for query in queryset:
            dto_list.append(
                LocationDTO(
                    name_city=query.name,
                    latitude=query.latitude,
                    longitude=query.longitude,
                    weather=self.get_forecast(query.latitude, query.longitude)
                ))
        return dto_list
