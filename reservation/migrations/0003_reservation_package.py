# Generated by Django 4.0.4 on 2022-04-14 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_remove_hotelpackage_period_hotelpackage_date_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='reservation.hotelpackage'),
        ),
    ]
