# Generated by Django 5.1.2 on 2024-11-24 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0079_staff_monthly_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='asset_source',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='no_staff',
        ),
    ]
