# Generated by Django 5.1.3 on 2024-11-23 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_order_user'),
        ('naija_kitchen', '0012_alter_restaurant_restaurant_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='naija_kitchen.restaurant'),
        ),
    ]
