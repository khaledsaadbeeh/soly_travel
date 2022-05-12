# Generated by Django 4.0.4 on 2022-05-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_organization_name_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number_2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='phone2'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('gold', 'GOLD'), ('silver', 'SILVER'), ('bronze', 'BRONZE')], max_length=20, verbose_name='role'),
        ),
    ]
