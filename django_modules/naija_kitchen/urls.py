from django.urls import include, path
from naija_kitchen.views import *
from naija_kitchen import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'menucategories', views.MenuCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


