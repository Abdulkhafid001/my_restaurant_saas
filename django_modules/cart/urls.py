from django.urls import path
from cart import views

urlpatterns = [
    path("update_cart/", views.update_cart, name="update_cart"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
]
