from naijakitchen_auth import views
from django.urls import path

urlpatterns = [
    path("signup/", views.test_server, name="signup")
]
