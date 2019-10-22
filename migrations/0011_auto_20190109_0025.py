# Generated by Django 2.1.3 on 2019-01-08 19:25

from django.db import migrations, models
import ecomapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0010_product_indications'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='contraindications',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='selection_of_sizes',
            field=models.ImageField(null=True, upload_to=ecomapp.models.image_folder),
        ),
    ]