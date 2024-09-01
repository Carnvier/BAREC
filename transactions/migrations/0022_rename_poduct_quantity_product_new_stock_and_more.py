# Generated by Django 4.2 on 2024-09-01 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0046_rename_purchase_details_purchases_details_and_more'),
        ('transactions', '0021_remove_stock_price_product_alter_sales_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='poduct_quantity',
            new_name='new_stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='poduct_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_branch',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_project',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='quantity',
        ),
        migrations.AddField(
            model_name='stock',
            name='product_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='company.branch'),
        ),
        migrations.AddField(
            model_name='stock',
            name='product_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='stock',
            name='product_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='company.projects'),
        ),
        migrations.AddField(
            model_name='stock',
            name='product_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='transactions.stock'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0.0)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesitem', to='transactions.stock')),
            ],
        ),
    ]