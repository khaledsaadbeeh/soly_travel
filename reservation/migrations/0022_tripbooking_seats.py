# Generated by Django 4.0.4 on 2022-04-29 15:07

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0021_alter_trip_accommodation_alter_trip_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripbooking',
            name='seats',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
