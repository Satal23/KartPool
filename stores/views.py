from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .services import get_nearby_stores_within
from .models import Store
from .serializers import NearbyStoreSerializer
# Create your views here.
class StoreView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = NearbyStoreSerializer

    def list(self, request):
        # Extract latitude and longitude information from the request query params
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')
        
        radius = 10 # in kilometres
        number_of_stores_to_return = 100

        stores = get_nearby_stores_within(
            lat=float(lat),
            lon=float(lon),
            km=radius,
            limit=number_of_stores_to_return
        )

        stores_data = NearbyStoreSerializer(stores, many=True)
        return Response(stores_data.data)
