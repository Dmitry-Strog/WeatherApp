from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from apps.weather.forms import CitySearchForm
from .dto import LocationDTO
from .exceptions import WeatherApiException
from .services.location_service import LocationService
from .services.weather_api_service import WeatherApiService


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = CitySearchForm
    success_url = reverse_lazy('weather:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = kwargs.get('form', CitySearchForm())
        context['user'] = self.request.user
        context['weather'] = WeatherApiService().location_forecast_dto(user_id=self.request.user.id)
        return context

    def form_valid(self, form):
        latitude = Decimal(self.request.POST['lat'])
        longitude = Decimal(self.request.POST['lon'])
        city = form.cleaned_data['city']
        dto_object = LocationDTO(
            name_city=city,
            latitude=latitude,
            longitude=longitude,
            user=self.request.user)
        try:
            LocationService.save_location(dto_object)
        except IntegrityError:
            form.add_error(None, "Локация с такими координатами уже существует для этого пользователя.")
            return self.form_invalid(form)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        try:
            context = self.get_context_data()
        except WeatherApiException:
            return render(self.request, "error.html")
        return self.render_to_response(context)


class SearchResultView(LoginRequiredMixin, FormView):
    template_name = 'city_search_results.html'
    form_class = CitySearchForm
    success_url = reverse_lazy('weather:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        city = form.cleaned_data['city']
        try:
            weather_json = WeatherApiService().get_location_by_name(city)
        except WeatherApiException:
            return render(self.request, "error.html")
        context = self.get_context_data()
        context['weather'] = weather_json
        return self.render_to_response(context)


class DeleteLocationView(LoginRequiredMixin, View):
    success_url = reverse_lazy('weather:home')

    def post(self, request, *args, **kwargs):
        city = request.POST.get('city')
        latitude = Decimal(request.POST.get('lat'))
        longitude = Decimal(request.POST.get('lon'))

        location_dto = LocationDTO(
            user=self.request.user.id,
            name_city=city,
            latitude=latitude,
            longitude=longitude,
        )

        LocationService.delete_location(location_dto)

        return redirect(self.success_url)
