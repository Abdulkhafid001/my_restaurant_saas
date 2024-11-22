from django.db.models.signals import post_save
from django.dispatch import receiver
from naija_kitchen.models import Restaurant, MenuCategory

# Signal receiver function


@receiver(post_save, sender=Restaurant)
def create_default_categories(sender, instance, created, **kwargs):
    if created:  # This ensures it only runs when a new Restaurant is created
        MenuCategory.objects.bulk_create([
            MenuCategory(restaurant=instance, name='Breakfast',
                         description='Start your day with a good breakfast'),
            MenuCategory(restaurant=instance, name='Lunch',
                         description='Enjoy a hearty lunch'),
            MenuCategory(restaurant=instance, name='Dinner',
                         description='End your day with a delightful dinner'),
        ])
