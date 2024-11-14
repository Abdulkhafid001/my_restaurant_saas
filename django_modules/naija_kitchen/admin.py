from django.contrib import admin
from naija_kitchen.models import *
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "restaurant_name",
        "restaurant_address",
    )

admin.site.register(Restaurant, RestaurantAdmin)