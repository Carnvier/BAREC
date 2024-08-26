# Generated by Django 4.2 on 2024-08-20 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_remove_debitors_debt_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branch_supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='company.staff'),
        ),
    ]