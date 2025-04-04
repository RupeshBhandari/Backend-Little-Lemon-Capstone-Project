# Generated by Django 5.1.7 on 2025-03-23 23:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
