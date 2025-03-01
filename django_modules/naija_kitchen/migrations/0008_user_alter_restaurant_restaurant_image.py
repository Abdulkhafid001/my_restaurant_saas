# Generated by Django 5.1.3 on 2024-11-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naija_kitchen', '0007_alter_menucategory_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
