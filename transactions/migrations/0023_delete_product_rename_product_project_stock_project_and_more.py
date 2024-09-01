# Generated by Django 4.2 on 2024-09-01 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0046_rename_purchase_details_purchases_details_and_more'),
        ('transactions', '0022_rename_poduct_quantity_product_new_stock_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='product_project',
            new_name='project',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='product_branch',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='product_quantity',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='stock',
        ),
        migrations.AlterField(
            model_name='stock',
            name='product_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='company.assets'),
        ),
    ]