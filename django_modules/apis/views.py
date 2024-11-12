from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from naija_kitchen.models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
