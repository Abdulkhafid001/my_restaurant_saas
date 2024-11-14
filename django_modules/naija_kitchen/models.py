from django.db import models


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    restaurant_address = models.CharField(max_length=200)
    restaurant_image = models.CharField(max_length=200)
    restaurant_contact = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.restaurant_name
