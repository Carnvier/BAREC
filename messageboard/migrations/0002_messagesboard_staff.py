# Generated by Django 4.2 on 2024-08-20 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_company_projects_assets_projects_and_more'),
        ('messageboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagesboard',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.staff'),
        ),
    ]
