# Generated by Django 4.2 on 2024-09-24 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0076_rename_email_organisationregistration_founder_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='headquaters',
            new_name='headquarters',
        ),
    ]