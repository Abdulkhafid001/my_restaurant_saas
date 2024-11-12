from rest_framework import serializers
from naija_kitchen.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("restaurant_name", "restaurant_address",
                  "restaurant_image", "restaurant_contact")
