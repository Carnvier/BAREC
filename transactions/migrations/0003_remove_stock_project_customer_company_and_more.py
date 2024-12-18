# Generated by Django 4.2 on 2024-08-20 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_remove_company_projects_assets_projects_and_more'),
        ('transactions', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='project',
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='liabilities',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.liabilities'),
        ),
        migrations.AddField(
            model_name='sales',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.stock'),
        ),
        migrations.AddField(
            model_name='stock',
            name='assets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='company.assets'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='branch',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='sales',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='transactions.stock'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='sales_rep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
