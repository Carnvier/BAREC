# Generated by Django 4.2 on 2024-08-27 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0028_remove_assets_asset_acquisition_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='company_description',
            new_name='organisation_description',
        ),
    ]
