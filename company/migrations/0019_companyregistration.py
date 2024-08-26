# Generated by Django 4.2 on 2024-08-24 15:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0018_alter_staff_staff_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('preffered_username', models.CharField(default='', max_length=255)),
                ('phone_number', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('organisation_name', models.CharField(default='', max_length=255)),
                ('est', models.DateField(default=django.utils.timezone.now)),
                ('headquaters', models.CharField(default='', max_length=255)),
                ('ID_Number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
