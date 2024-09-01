# Generated by Django 4.2 on 2024-08-30 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0043_remove_liabilities_supplier_liabilities_sources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchases',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='unit_price',
        ),
        migrations.CreateModel(
            name='Purchased_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('unit_price', models.IntegerField(default=0.0)),
                ('purchases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_purchased', to='company.purchases')),
            ],
        ),
    ]