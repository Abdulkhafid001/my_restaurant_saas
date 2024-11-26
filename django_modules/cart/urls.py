from django.urls import path
from cart import views
from cart.cartutils import test


urlpatterns = [
    path("update_cart/", views.update_cart, name="update_cart"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("test/", test, name="test"),
]
