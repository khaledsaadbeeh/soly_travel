# Generated by Django 4.0.4 on 2022-04-22 07:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_organization_profile_balance_profile_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='201111504980', max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number_2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]