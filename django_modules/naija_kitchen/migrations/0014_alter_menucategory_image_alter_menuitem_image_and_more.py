# Generated by Django 5.1.3 on 2024-12-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naija_kitchen', '0013_alter_restaurant_restaurant_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploaded_images'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_images'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_images'),
        ),
    ]