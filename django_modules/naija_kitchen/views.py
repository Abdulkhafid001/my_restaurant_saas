from django.shortcuts import render
from naija_kitchen.models import *
from naija_kitchen.serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'restaurant': reverse('restaurant-list', request=request, format=format),
    })


class RestaurantList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



