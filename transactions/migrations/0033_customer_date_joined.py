# Generated by Django 5.1.2 on 2024-11-24 12:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0032_sales_processing_fee_sales_tax_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_joined',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]