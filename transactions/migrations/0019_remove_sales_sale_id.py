# Generated by Django 4.2 on 2024-08-28 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0018_stock_branch_stock_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='sale_id',
        ),
    ]
