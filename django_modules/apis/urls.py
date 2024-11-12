from django.urls import path
from .views import RestaurantAPIView

urlpatterns = [
    path("", RestaurantAPIView.as_view(), name="restaurant_list")
]
