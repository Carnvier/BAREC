# Generated by Django 4.2 on 2024-08-30 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0037_rename_company_phone_number_company_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='CEO_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='company_email',
        ),
        migrations.RemoveField(
            model_name='company',
            name='phone_number',
        ),
    ]