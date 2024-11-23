# Generated by Django 5.1.3 on 2024-11-23 06:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naija_kitchen', '0011_menucategory_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
