# Generated by Django 4.2 on 2024-08-20 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_liabilities_suppliers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liabilities',
            old_name='suppliers',
            new_name='supplier',
        ),
        migrations.RemoveField(
            model_name='liabilities',
            name='creditor_name',
        ),
    ]
