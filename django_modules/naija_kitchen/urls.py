from django.urls import path
from naija_kitchen import views
urlpatterns = [
    path("", views.get_names, name="getFullNames")
]
