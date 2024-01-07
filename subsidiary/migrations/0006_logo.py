# Generated by Django 4.2.7 on 2023-12-07 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subsidiary', '0005_rename_propertydevelopment_subsidiaryimages_propertydevelopment1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo1', models.ImageField(default='default.jpg', upload_to='logo_images')),
                ('logo2', models.ImageField(default='default.jpg', upload_to='logo_images')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]