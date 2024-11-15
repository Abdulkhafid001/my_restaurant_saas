from django.urls import path
from naija_kitchen.views import ListRestaurant, RestaurantDetail
urlpatterns = [
    path("", ListRestaurant.as_view(), name="Get Restaurant Names"),
    path("restaurant/<int:pk>/", RestaurantDetail.as_view(), name="Get Restaurant Detail")
] 
