from rest_framework import serializers
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem


from rest_framework import serializers
from naija_kitchen.models import Restaurant, MenuCategory


class MenuCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['url', 'name', 'restaurant']


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    menu_categories = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='menucategory-detail'
    )

    class Meta:
        model = Restaurant
        fields = ['url', 'restaurant_name', 'menu_categories']


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
