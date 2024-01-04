# Generated by Django 4.2.7 on 2023-12-07 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subsidiary', '0006_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcomeImage', models.ImageField(default='default.jpg', upload_to='home_images')),
                ('contentImage1', models.ImageField(default='default.jpg', upload_to='home_images')),
                ('contentImage2', models.ImageField(default='default.jpg', upload_to='home_images')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
