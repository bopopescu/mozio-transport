# Generated by Django 2.1 on 2018-08-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_auto_20180821_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='area',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]