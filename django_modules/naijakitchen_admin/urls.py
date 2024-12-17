from django.urls import path
from . import views
urlpatterns = [
    path("admin/", views.get_admin_home, name="naijakitchenadminhome")
    
]
