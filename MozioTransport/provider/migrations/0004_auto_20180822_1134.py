# Generated by Django 2.1 on 2018-08-22 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0003_auto_20180821_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ('name',), 'verbose_name_plural': 'providers'},
        ),
        migrations.RemoveField(
            model_name='provider',
            name='created_at',
        ),
    ]
