from django.urls import include, path
from naija_kitchen.views import *
from naija_kitchen import views
from naija_kitchen.app_views.restaurant_views import RestaurantListView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'menucategories', views.MenuCategoryViewSet)

urlpatterns = [
    # path('', include(router.urls), name='api-home'),
    path('login', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("myrestaurants/", RestaurantListView.as_view(), name="all restaurants"),
    path("restaurant/<int:restaurant_id>/menucategories", views.get_restaurant_menucategories, name="restaurant menucategories"),
    path("menucategory/<int:menucategory_id>/menuitems", views.get_menucategory_items, name="restaurant menuitems")
]
