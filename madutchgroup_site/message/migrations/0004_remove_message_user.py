# Generated by Django 4.2.7 on 2023-11-30 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_message_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
    ]
