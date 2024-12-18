# Generated by Django 4.2 on 2024-09-22 16:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0067_debitor_salary_organisation_alter_staff_occupation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_brought_in', models.DateField(default=django.utils.timezone.now)),
                ('source', models.CharField(default='', max_length=50)),
                ('asset_name', models.CharField(default='', max_length=255)),
                ('type_of_asset', models.CharField(choices=[('Current Asset', 'Current Asset'), ('Fixed Asset', 'Fixed Asset')], default='Current Asset', max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('acquistion_price', models.IntegerField(default=0)),
                ('asset_value', models.IntegerField(default=0)),
                ('asset_source', models.CharField(default='', max_length=255)),
                ('depreciation_period', models.CharField(choices=[('Weekly', 'Weekly'), ('Bi-weekly', 'Bi-weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half-Yearly', 'Half-Yearly'), ('Yearly', 'Yearly')], default='Yearly', max_length=50)),
                ('depreciation_rate', models.IntegerField(default=0)),
                ('asset_status', models.CharField(choices=[('Active', 'Active'), ('Depreciated', 'Depreciated'), ('Disposed', 'Disposed')], default='Active', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Creditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sources', models.CharField(choices=[('Individual', 'Individual'), ('Corporate', 'Corporate'), ('Other', 'Other')], default='Other', max_length=50)),
                ('credit_acquisition_date', models.DateField(default='2024-08-10')),
                ('creditor', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(default='', max_length=255)),
                ('credit_type', models.CharField(choices=[('Long-term', 'Long-term'), ('Short-term', 'Short-term')], default='Short-term', max_length=255)),
                ('details', models.CharField(default='', max_length=50)),
                ('credit_amount', models.IntegerField(default=0)),
                ('credit_paid_status', models.BooleanField(default=False)),
                ('interest_rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Debtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_acquisition_date', models.DateField(auto_now_add=True)),
                ('receiver', models.CharField(max_length=50)),
                ('type_of_debt', models.CharField(choices=[('Short Term', 'Short Term'), ('Long Term', 'Long Term')], default='Short Term', max_length=255)),
                ('details', models.TextField(default='')),
                ('amount', models.IntegerField(default=0)),
                ('paid_status', models.BooleanField(default=False)),
                ('interest_period', models.CharField(choices=[('Weekly', 'Weekly'), ('Bi-weekly', 'Bi-weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half-Yearly', 'Half-Yearly'), ('Yearly', 'Yearly')], default='Monthly', max_length=50)),
                ('interest_rate', models.IntegerField(default=0)),
                ('amount_paid', models.FloatField(default=0.0)),
            ],
        ),
        migrations.RemoveField(
            model_name='assets',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='assets',
            name='organisation',
        ),
        migrations.RemoveField(
            model_name='assets',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='assets',
            name='source',
        ),
        migrations.RemoveField(
            model_name='debitor',
            name='assets',
        ),
        migrations.RemoveField(
            model_name='debitor',
            name='debitor',
        ),
        migrations.RemoveField(
            model_name='debitor',
            name='organisation',
        ),
        migrations.RemoveField(
            model_name='liabilities',
            name='organisation',
        ),
        migrations.RemoveField(
            model_name='liabilities',
            name='projects',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='staff_project',
            new_name='project',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='cash_in_hand',
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='staff_branch',
        ),
        migrations.AddField(
            model_name='staff',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
