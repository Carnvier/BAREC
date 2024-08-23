# Generated by Django 4.2 on 2024-08-20 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_remove_company_projects_assets_projects_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='company',
        ),
        migrations.AddField(
            model_name='organisation',
            name='founder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organisations', to=settings.AUTH_USER_MODEL),
        ),
    ]
