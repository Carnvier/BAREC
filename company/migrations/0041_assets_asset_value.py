# Generated by Django 4.2 on 2024-08-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0040_rename_asset_price_assets_acquistion_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='asset_value',
            field=models.IntegerField(default=0),
        ),
    ]
