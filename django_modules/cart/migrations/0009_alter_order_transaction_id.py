# Generated by Django 5.1.3 on 2025-01-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_order_status_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]