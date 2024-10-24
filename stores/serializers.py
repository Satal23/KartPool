from rest_framework import serializers
from django.contrib.auth.models import User
from stores.models import Store

# Define StoreSerializer first
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'id', 'name', 'rating', 'opening_hour', 'closing_hour', 'store_type',
            'address', 'lat', 'lon',
        ]

# Now define NearbyStoreSerializer
class NearbyStoreSerializer(StoreSerializer):
    distance = serializers.SerializerMethodField()

    def get_distance(self, instance):
        return instance.distance.mi if instance else 'N/A'

    class Meta(StoreSerializer.Meta):  # Use StoreSerializer's Meta class
        fields = StoreSerializer.Meta.fields + ['distance']  # Include the distance field
