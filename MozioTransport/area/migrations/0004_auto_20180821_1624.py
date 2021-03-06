# Generated by Django 2.1 on 2018-08-21 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0003_auto_20180821_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(message='Please enter a decimal number.', regex='^\\d+\\.\\d+$')]),
        ),
        migrations.AlterField(
            model_name='area',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(message='Please enter a decimal number.', regex='^\\d+\\.\\d+$')]),
        ),
    ]
