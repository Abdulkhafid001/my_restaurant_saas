from rest_framework import serializers
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

# class RestaurantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Restaurant
#         fields = "__all__"


# class MenuCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuCategory
#         fields = "__all__"


# class MenuItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuItem
#         fields = "__all__"
