# Generated by Django 4.2 on 2024-09-22 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0068_asset_creditor_debtor_remove_assets_branch_and_more'),
        ('transactions', '0031_remove_sales_branch_remove_stock_branch_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Assets',
        ),
        migrations.DeleteModel(
            name='Debitor',
        ),
        migrations.DeleteModel(
            name='Liabilities',
        ),
        migrations.AddField(
            model_name='debtor',
            name='assets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.asset'),
        ),
        migrations.AddField(
            model_name='debtor',
            name='debtor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debtors', to='transactions.customer'),
        ),
        migrations.AddField(
            model_name='debtor',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debtors', to='company.organisation'),
        ),
        migrations.AddField(
            model_name='debtor',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debtors', to='company.projects'),
        ),
        migrations.AddField(
            model_name='creditor',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liabilities', to='company.organisation'),
        ),
        migrations.AddField(
            model_name='creditor',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liabilities', to='company.projects'),
        ),
        migrations.AddField(
            model_name='asset',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='company.organisation'),
        ),
        migrations.AddField(
            model_name='asset',
            name='projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='company.projects'),
        ),
    ]
