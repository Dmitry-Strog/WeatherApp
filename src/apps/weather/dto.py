from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Dict


@dataclass
class LocationDTO:
    name_city: str
    latitude: Decimal
    longitude: Decimal
    id: int = None
    user: int = None
    weather: Optional[Dict] = None
