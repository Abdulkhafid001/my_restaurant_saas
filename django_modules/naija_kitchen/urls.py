from django.urls import path
from naija_kitchen.views import *
from naija_kitchen import views
urlpatterns = [
    path("", views.api_root, name="restaurant-list"),
    path('restaurant/',views.RestaurantList.as_view(),name=''),
    path('restaurant/<int:pk>/',views.RestaurantDetail.as_view(),name=''),
   
]
