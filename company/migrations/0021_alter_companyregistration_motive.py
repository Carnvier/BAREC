# Generated by Django 4.2 on 2024-08-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0020_companyregistration_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyregistration',
            name='motive',
            field=models.TextField(default='', max_length=255),
        ),
    ]
