# Generated by Django 4.2 on 2024-08-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0006_remove_messagesboard_message_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagesboard',
            name='ref',
            field=models.CharField(max_length=25),
        ),
    ]
