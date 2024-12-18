# Generated by Django 4.2 on 2024-08-29 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0033_assets_quantity'),
        ('transactions', '0020_remove_customer_customer_id_alter_customer_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='price',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=255)),
                ('poduct_quantity', models.IntegerField(default=0)),
                ('poduct_price', models.FloatField(default=0.0)),
                ('product_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='company.branch')),
                ('product_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='company.projects')),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='transactions.stock')),
            ],
        ),
        migrations.AlterField(
            model_name='sales',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.product'),
        ),
    ]
