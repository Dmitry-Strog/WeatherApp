from django.db.models import QuerySet

from apps.weather.dto import LocationDTO
from apps.weather.models import Location


class LocationService:

    @staticmethod
    def save_location(dto: LocationDTO) -> QuerySet:
        return Location.objects.create(
            name=dto.name_city,
            user=dto.user,
            latitude=dto.latitude,
            longitude=dto.longitude
        )

    @staticmethod
    def get_all_locations(user_id: int) -> QuerySet:
        return Location.objects.filter(user=user_id).all()

    @staticmethod
    def delete_location(dto: LocationDTO) -> QuerySet:
        return Location.objects.filter(user_id=dto.user).get(latitude=dto.latitude, longitude=dto.longitude).delete()
