# Generated by Django 2.1.3 on 2019-01-08 17:00

from django.db import migrations, models
import ecomapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0008_auto_20190108_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=1, upload_to=ecomapp.models.image_folder),
            preserve_default=False,
        ),
    ]
