from decimal import Decimal
from unittest.mock import Mock, patch
from django.test import TestCase

from apps.weather.exceptions import WeatherApiException
from apps.weather.services.weather_api_service import WeatherApiService


class WeatherApiServiceTest(TestCase):
    def setUp(self):
        self.response_api_location = {
            "name": "Los Angeles",
            "local_names": {
                "ru": "Лос-Анджелес",
            },
            "lat": 34.0537,
            "lon": -118.2428,
            "country": "US",
            "state": "California"
        }
        self.response_api_forecast = {
            "coord": {
                "lon": -118.2428,
                "lat": 34.0537
            },
            "weather": {
                "id": 711,
                "temp": 20.69,
                "main": "Smoke",
                "description": "дымка",
            }
            ,
            "name": "Лос-Анджелес",
        }

    @patch("requests.get")
    def test_get_location(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.response_api_location
        mock_get.return_value = mock_response

        api_response = WeatherApiService.get_location_by_name("Los Angeles")
        self.assertEqual(api_response["name"], "Los Angeles")
        self.assertEqual(api_response["country"], "US")
        self.assertEqual(api_response["lat"], 34.0537)
        self.assertEqual(api_response["lon"], -118.2428)
        self.assertEqual(api_response, self.response_api_location)

    @patch("requests.get")
    def test_get_forecast_by_coord(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.response_api_forecast
        mock_get.return_value = mock_response

        api_response = WeatherApiService.get_forecast_by_coord(Decimal(34.0537), Decimal(-118.2428))
        self.assertEqual(api_response["name"], "Лос-Анджелес")
        self.assertEqual(api_response["weather"]["temp"], 20.69)
        self.assertEqual(api_response["coord"]["lat"], 34.0537)
        self.assertEqual(api_response["coord"]["lon"], -118.2428)
        self.assertEqual(api_response, self.response_api_forecast)

    @patch("requests.get")
    def test_get_location_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 403
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        with self.assertRaises(WeatherApiException):
            WeatherApiService.get_location_by_name("")
