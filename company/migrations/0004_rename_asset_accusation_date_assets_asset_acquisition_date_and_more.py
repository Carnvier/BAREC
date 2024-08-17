# Generated by Django 4.2 on 2024-08-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_rename_project_locations_projects_project_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets',
            old_name='asset_accusation_date',
            new_name='asset_acquisition_date',
        ),
        migrations.RenameField(
            model_name='debitors',
            old_name='debit_accusation_date',
            new_name='debt_acquisition_date',
        ),
        migrations.RenameField(
            model_name='debitors',
            old_name='debited_amount',
            new_name='debt_amount',
        ),
        migrations.RenameField(
            model_name='debitors',
            old_name='debit_source',
            new_name='debt_source',
        ),
        migrations.RenameField(
            model_name='debitors',
            old_name='type_of_debit',
            new_name='type_of_debt',
        ),
        migrations.RenameField(
            model_name='liabilities',
            old_name='liability_name',
            new_name='Creditor_name',
        ),
        migrations.RenameField(
            model_name='liabilities',
            old_name='liablity_accusation_date',
            new_name='liablity_acquisition_date',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='staff_salary',
            new_name='monthly_salary',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='address',
        ),
        migrations.AlterField(
            model_name='assets',
            name='type_of_asset',
            field=models.CharField(choices=[('Current Asset', 'Current Asset'), ('Fixed Asset', 'Fixed Asset')], max_length=255),
        ),
        migrations.AlterField(
            model_name='liabilities',
            name='type_of_liability',
            field=models.CharField(choices=[('Long-term', 'Long-term'), ('Short-term', 'Short-term')], max_length=255),
        ),
    ]
