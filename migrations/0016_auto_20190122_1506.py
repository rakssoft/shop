# Generated by Django 2.1.1 on 2019-01-22 10:06

from django.db import migrations, models
import ecomapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0015_images_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image',
        ),
        migrations.AddField(
            model_name='images',
            name='image_fb',
            field=models.ImageField(default=1, upload_to=ecomapp.models.image_folder),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='image_phone',
            field=models.ImageField(default=1, upload_to=ecomapp.models.image_folder),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='image_vk',
            field=models.ImageField(default=1, upload_to=ecomapp.models.image_folder),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='image_whatsapp',
            field=models.ImageField(default=1, upload_to=ecomapp.models.image_folder),
            preserve_default=False,
        ),
    ]