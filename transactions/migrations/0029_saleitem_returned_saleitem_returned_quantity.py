# Generated by Django 4.2 on 2024-09-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0028_saleitem_organisation_alter_saleitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleitem',
            name='returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleitem',
            name='returned_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
