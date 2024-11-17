from rest_framework import viewsets
from naija_kitchen.models import Restaurant, MenuCategory
from naija_kitchen.serializers import RestaurantSerializer, MenuCategorySerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
