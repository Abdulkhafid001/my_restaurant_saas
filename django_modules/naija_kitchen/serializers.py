from rest_framework import serializers
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem


from rest_framework import serializers
from naija_kitchen.models import Restaurant, MenuCategory


class MenuCategorySerializer(serializers.HyperlinkedModelSerializer):
    menu_items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='menuitem-detail'
    )

    class Meta:
        model = MenuCategory
        fields = ['url', 'name', 'menu_items']


# class MenuItemSerializer(serializers.HyperlinkedModelSeriali  zer):
#     menu_categories = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='menucategory-detail'
#     )
#     class Meta:
#         model = MenuItem
#         fields = ['url', 'name', 'menu_categories']


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
