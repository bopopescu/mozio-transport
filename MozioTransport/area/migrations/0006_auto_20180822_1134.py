# Generated by Django 2.1 on 2018-08-22 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0005_auto_20180821_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='area',
            name='longitude',
        ),
    ]
