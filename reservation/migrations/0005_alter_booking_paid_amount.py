# Generated by Django 4.0.4 on 2022-04-15 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_booking_bookingerror_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='paid_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=36, null=True, verbose_name='paid amount'),
        ),
    ]
