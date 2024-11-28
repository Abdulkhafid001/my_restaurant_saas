from django.contrib import admin
from naija_kitchen.models import *
from cart.models import *
from django.contrib.sessions.models import Session
admin.site.register(Session)

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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date_ordered',
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'product',
        'quantity',
        'date_added',
    )
