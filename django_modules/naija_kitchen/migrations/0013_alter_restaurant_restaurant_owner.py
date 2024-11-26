# Generated by Django 5.1.3 on 2024-11-26 08:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naija_kitchen', '0012_alter_restaurant_restaurant_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_restaurants', to=settings.AUTH_USER_MODEL),
        ),
    ]
