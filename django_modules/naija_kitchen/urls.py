from django.urls import path
from naija_kitchen.views import *
urlpatterns = [
    path("", ListRestaurant.as_view(), name="Restaurant Names"),
    path("restaurant/<int:pk>/", RestaurantDetail.as_view(), name="Restaurant Detail"),
    path("restaurant/<int:pk>/categories", ListMenuCategory.as_view(), name="Menu Category"),
    path("restaurant/<int:pk>/categories/menuitem", ListMenuItem.as_view(), name="Menu Item")
]
