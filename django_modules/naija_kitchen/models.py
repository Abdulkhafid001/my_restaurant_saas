from django.db import models
from django.db.models import UniqueConstraint
from django.utils.text import slugify


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    restaurant_address = models.CharField(max_length=200)
    restaurant_image = models.ImageField(
        null=True, blank=True, upload_to='uploaded_images')
    restaurant_contact = models.CharField(max_length=200)
    restaurant_owner = models.ForeignKey(
        'auth.User', blank=True, null=True, on_delete=models.CASCADE, related_name='user_restaurants')

    class Meta:
        ordering = ['restaurant_name']
        indexes = [
            models.Index(fields=['restaurant_name'])
        ]

    def __str__(self) -> str:
        return self.restaurant_name

    @property
    def imageURL(self):
        try:
            url = self.restaurant_image.url
        except:
            url = ''
        return url


class MenuCategory(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menu_categories')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True,
                              upload_to='static/uploaded_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['restaurant', 'name'],
                             name='unique_category_per_restaurant')
        ]
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return f"{self.name} ({self.restaurant.restaurant_name})"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class MenuItem(models.Model):
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True,
                              upload_to='uploaded_images')

    def save(self, *args, **kwargs):
        # Automatically generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class User(models.Model):
    user_name = models.CharField(max_length=200, null=False)
    user_email = models.EmailField(null=False)

    def __str__(self):
        return f"username: {self.user_name}, mail: {self.user_email}"
