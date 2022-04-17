# Generated by Django 4.0.4 on 2022-04-14 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelpackage',
            name='period',
        ),
        migrations.AddField(
            model_name='hotelpackage',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotelpackage',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
