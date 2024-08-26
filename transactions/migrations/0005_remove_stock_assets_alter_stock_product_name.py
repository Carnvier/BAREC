# Generated by Django 4.2 on 2024-08-20 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_remove_debitors_debt_source'),
        ('transactions', '0004_remove_customer_company_customer_organisation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='assets',
        ),
        migrations.AlterField(
            model_name='stock',
            name='product_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='company.assets'),
        ),
    ]