# Generated by Django 4.2.7 on 2023-12-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsidiary', '0004_subsidiaryimages_propertydevelopment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsidiaryimages',
            old_name='propertyDevelopment',
            new_name='propertyDevelopment1',
        ),
        migrations.AddField(
            model_name='subsidiaryimages',
            name='propertyDevelopment2',
            field=models.ImageField(default='default.jpg', upload_to='property_development_images'),
        ),
        migrations.AddField(
            model_name='subsidiaryimages',
            name='propertyDevelopment3',
            field=models.ImageField(default='default.jpg', upload_to='property_development_images'),
        ),
        migrations.AddField(
            model_name='subsidiaryimages',
            name='propertyDevelopment4',
            field=models.ImageField(default='default.jpg', upload_to='property_development_images'),
        ),
        migrations.AddField(
            model_name='subsidiaryimages',
            name='propertyDevelopment5',
            field=models.ImageField(default='default.jpg', upload_to='property_development_images'),
        ),
    ]