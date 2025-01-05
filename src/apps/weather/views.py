from decimal import Decimal

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.weather.forms import CitySearchForm
from .dto import LocationDTO
from .services.location_service import LocationService
from .services.weather_api_service import WeatherApiService


def home_page(request):
    form = CitySearchForm()
    if request.method == 'POST':
        latitude = Decimal(request.POST['lat'])
        longitude = Decimal(request.POST['lon'])
        city = request.POST['city']
        dto = LocationDTO(
            name_city=city,
            latitude=latitude,
            longitude=longitude,
            user=request.user)
        LocationService.save_location(dto)
    location = WeatherApiService().location_forecast_dto(user_id=request.user.id)
    context = {
        'user': request.user,
        'form': form,
        'weather': location,
    }
    return render(request, "home.html", context)


def search_result(request):
    weather_json = None
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user:login'))

        form = CitySearchForm(data=request.POST)
        if form.is_valid():
            city = request.POST['city']
            weather_json = WeatherApiService().get_cities(city)

    else:
        form = CitySearchForm()

    context = {
        'user': request.user,
        'form': form,
        'weather': weather_json,
    }
    return render(request, "city_search_results.html", context)


def delete_forecast(request):
    if request.method == 'POST':
        city = request.POST['city']
        latitude = Decimal(request.POST['lat'])
        longitude = Decimal(request.POST['lon'])
        LocationService.delete_location(LocationDTO(
            name_city=city,
            latitude=latitude,
            longitude=longitude,
        ))
    return redirect('weather:home')
