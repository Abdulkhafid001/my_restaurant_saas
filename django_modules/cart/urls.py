from django.urls import path
from .views import update_cart, cart, checkout

urlpatterns = [
    path("update_cart/", update_cart, name="update_cart"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
]
