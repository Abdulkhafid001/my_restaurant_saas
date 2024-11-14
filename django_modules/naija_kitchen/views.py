from django.shortcuts import render
from naija_kitchen.models import *
from naija_kitchen.serializers import *
from rest_framework import generics
# Create your views here.


class ListRestaurant(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
