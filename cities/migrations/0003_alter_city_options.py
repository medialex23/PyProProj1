# Generated by Django 3.2 on 2021-05-19 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20210506_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('name',), 'verbose_name': 'Місто', 'verbose_name_plural': 'Міста'},
        ),
    ]
