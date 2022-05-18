# Generated by Django 4.0.4 on 2022-05-17 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0031_alter_booking_date_from_alter_booking_date_until'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('cancelled', 'CANCELLED')], default=('active', 'ACTIVE'), max_length=10),
        ),
        migrations.AddField(
            model_name='tripbooking',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('cancelled', 'CANCELLED')], default=('active', 'ACTIVE'), max_length=10),
        ),
        migrations.AddField(
            model_name='tripprogram',
            name='cost',
            field=models.PositiveIntegerField(default=120, verbose_name='cost'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotelpackage',
            name='date_from',
            field=models.DateField(verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='hotelpackage',
            name='date_until',
            field=models.DateField(verbose_name='To'),
        ),
        migrations.AlterField(
            model_name='hotelpackage',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='packages', to='reservation.hotel', verbose_name='Hotel'),
        ),
        migrations.AlterField(
            model_name='hotelpackage',
            name='label',
            field=models.CharField(max_length=50, verbose_name='label'),
        ),
        migrations.AlterField(
            model_name='tripbooking',
            name='seats',
            field=models.TextField(blank=True, null=True, verbose_name='Seats'),
        ),
        migrations.AlterField(
            model_name='tripprogram',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tripprogram',
            name='price',
            field=models.PositiveIntegerField(verbose_name='price'),
        ),
    ]
