# Generated by Django 4.2 on 2024-08-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0030_rename_company_name_email_company_company_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branch_name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
