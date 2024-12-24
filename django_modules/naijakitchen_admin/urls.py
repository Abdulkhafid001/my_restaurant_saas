from django.urls import path
from . import views
urlpatterns = [
    path("admin/", views.get_admin_home, name="naijakitchenadminhome"),
    path("admin/addcategory", views.add_menu_category, name="add_category"),
]
