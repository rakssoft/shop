# Generated by Django 2.1.1 on 2019-01-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0014_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
