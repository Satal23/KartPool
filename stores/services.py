from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry

from .models import Store

def get_nearby_stores_within(lat: float, lon: float, km: int=10, limit: int=None, srid: int=4326):
    coordinates = Point(lon, lat, srid=srid)
    point = GEOSGeometry(coordinates, srid=4326)
    return Store.objects.annotate(
            distance=Distance("location", coordinates
        )).filter(
            location__distance_lte=(point, D(km=km))
        ).order_by(
            'distance'
        )[0:limit]