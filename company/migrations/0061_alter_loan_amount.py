# Generated by Django 4.2 on 2024-09-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0060_loan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]