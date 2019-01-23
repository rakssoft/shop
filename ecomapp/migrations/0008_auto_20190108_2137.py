# Generated by Django 2.1.3 on 2019-01-08 16:37

from django.db import migrations, models
import ecomapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_auto_20190108_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to=ecomapp.models.image_folder),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
