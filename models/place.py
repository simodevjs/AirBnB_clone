#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """A class that represents a place."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0  # Added for completeness, imilar attributes.
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # Correcteds' to 'amenity_ids'
