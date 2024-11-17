from rest_framework import serializers
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem


from rest_framework import serializers
from naija_kitchen.models import Restaurant, MenuCategory


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    menu_categories = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='menucategory-detail'
    )

    class Meta:
        model = Restaurant
        fields = ['url', 'restaurant_name',
                  'menu_categories', 'restaurant_address']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'is_available']


class MenuCategorySerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(
        many=True, read_only=True)

    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description', 'menu_items']
