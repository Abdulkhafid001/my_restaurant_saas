from django.contrib import admin
from naija_kitchen.models import *
# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "restaurant_name",
        "restaurant_address",
    )
    prepopulated_fields = {'slug': ('restaurant_name',)}


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'is_available'
    )
    list_filter = ['is_available', 'created_at', 'updated_at']
    list_editable = ['price', 'is_available']
    prepopulated_fields = {'slug': ('name',)}


# admin.site.register(MenuItem)
# admin.site.register(MenuCategory)
# admin.site.register(Restaurant, RestaurantAdmin)
