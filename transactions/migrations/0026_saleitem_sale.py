# Generated by Django 4.2 on 2024-09-01 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0025_stock_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleitem',
            name='sale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_item', to='transactions.sales'),
        ),
    ]