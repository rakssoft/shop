# Generated by Django 2.1.3 on 2019-01-08 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0009_product_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='indications',
            field=models.TextField(null=True),
        ),
    ]
