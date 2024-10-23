# Generated by Django 4.2 on 2024-09-24 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0073_organisationregistration_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisationregistration',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]