# Generated by Django 4.2 on 2024-09-01 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0047_staff_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='company.organisation'),
        ),
    ]
