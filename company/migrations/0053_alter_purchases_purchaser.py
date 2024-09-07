# Generated by Django 4.2 on 2024-09-07 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0052_rename_project_name_projects_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='purchaser',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL),
        ),
    ]