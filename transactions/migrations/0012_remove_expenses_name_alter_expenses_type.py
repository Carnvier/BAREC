# Generated by Django 4.2 on 2024-08-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_alter_expenses_liabilities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='name',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='type',
            field=models.CharField(choices=[('Running Expense', 'Running Expense'), ('Repairs', 'Repairs'), ('Salary', 'Salary'), ('Loans', 'Loans')], max_length=255),
        ),
    ]
