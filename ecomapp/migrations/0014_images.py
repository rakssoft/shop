# Generated by Django 2.1.1 on 2019-01-17 07:28

from django.db import migrations, models
import ecomapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0013_auto_20190113_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('image', models.ImageField(null=True, upload_to=ecomapp.models.image_folder)),
            ],
        ),
    ]
