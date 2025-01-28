from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Dict


@dataclass
class LocationDTO:
    name_city: str = None
    latitude: Decimal = None
    longitude: Decimal = None
    user: int = None
    weather: Optional[Dict] = None
