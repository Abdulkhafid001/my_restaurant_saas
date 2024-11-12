from django.urls import path
from naija_kitchen.views import RestaurantListView
urlpatterns = [
    path("restaurants/", RestaurantListView.as_view(), name="Get Restaurant Names")
]
