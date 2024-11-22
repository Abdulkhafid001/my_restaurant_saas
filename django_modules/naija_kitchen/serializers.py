from rest_framework import serializers
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem
from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    menu_categories = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='menucategory-detail'
    )

    class Meta:
        model = Restaurant
        fields = ['url', 'restaurant_name',
                  'restaurant_address', 'menu_categories',]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'is_available']


class MenuCategorySerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(
        many=True, read_only=True)
    restaurant_data = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='restaurant-list'
    )

    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description', 'restaurant_data', 'menu_items']
