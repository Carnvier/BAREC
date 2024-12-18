# Generated by Django 4.2 on 2024-09-19 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0030_alter_customer_email'),
        ('company', '0063_liabilities_creditor_liabilities_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='amount_paid',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='loan',
            name='borrower',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='transactions.customer'),
        ),
        migrations.AddField(
            model_name='loan',
            name='interest_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='loan',
            name='organisation',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='company.organisation'),
        ),
    ]
