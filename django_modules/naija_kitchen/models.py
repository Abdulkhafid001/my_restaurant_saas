from django.db import models
from django.db.models import UniqueConstraint


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    restaurant_address = models.CharField(max_length=200)
    restaurant_image = models.CharField(max_length=200)
    restaurant_contact = models.CharField(max_length=200)
    restaurant_owner = models.ForeignKey(
        'auth.User', blank=True, null=True, on_delete=models.CASCADE, related_name='restaurant_name')

    def __str__(self) -> str:
        return self.restaurant_name


class MenuCategory(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menu_categories')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['restaurant', 'name'],
                             name='unique_category_per_restaurant')
        ]

    def __str__(self):
        return f"{self.name} ({self.restaurant.restaurant_name})"


class MenuItem(models.Model):
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name
