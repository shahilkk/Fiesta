# Generated by Django 4.0 on 2022-04-22 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='priceper_head',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='priceper_kg',
            field=models.IntegerField(),
        ),
    ]
