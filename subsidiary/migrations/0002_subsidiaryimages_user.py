# Generated by Django 4.2.7 on 2023-12-07 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subsidiary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsidiaryimages',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]