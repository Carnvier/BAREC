# Generated by Django 4.2 on 2024-09-22 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0030_alter_customer_email'),
        ('company', '0066_remove_staff_monthly_salary_remove_staff_staff_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_acquisition_date', models.DateField(auto_now_add=True)),
                ('type_of_debt', models.CharField(choices=[('Short Term', 'Short Term'), ('Long Term', 'Long Term')], default='Short Term', max_length=255)),
                ('debt_amount', models.IntegerField(default=0)),
                ('debt_paid_status', models.BooleanField(default=False)),
                ('interest_period', models.CharField(choices=[('Weekly', 'Weekly'), ('Bi-Weekly', 'Bi-Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annual', 'Annual')], default='Monthly', max_length=50)),
                ('interest_rate', models.IntegerField(default=0)),
                ('assets', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.assets')),
                ('debitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debitors', to='transactions.customer')),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debitors', to='company.organisation')),
            ],
        ),
        migrations.AddField(
            model_name='salary',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salaries', to='company.organisation'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='occupation',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_project',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='company.projects'),
        ),
        migrations.DeleteModel(
            name='Debitors',
        ),
    ]