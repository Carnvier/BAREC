# Generated by Django 4.2 on 2024-09-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0056_rename_branch_name_branch_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='tax_percentage',
            field=models.IntegerField(default=0.0),
        ),
    ]