# Generated by Django 4.2 on 2024-08-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0032_alter_liabilities_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]