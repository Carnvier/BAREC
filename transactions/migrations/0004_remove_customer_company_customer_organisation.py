# Generated by Django 4.2 on 2024-08-20 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_remove_projects_supervisor_and_more'),
        ('transactions', '0003_remove_stock_project_customer_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='company',
        ),
        migrations.AddField(
            model_name='customer',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='company.organisation'),
        ),
    ]
