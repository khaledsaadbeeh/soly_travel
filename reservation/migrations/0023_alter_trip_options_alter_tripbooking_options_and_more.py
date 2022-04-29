# Generated by Django 4.0.4 on 2022-04-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0022_tripbooking_seats'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trip',
            options={'ordering': ['-creation_date']},
        ),
        migrations.AlterModelOptions(
            name='tripbooking',
            options={'ordering': ['-creation_date']},
        ),
        migrations.AlterField(
            model_name='tripbooking',
            name='seats',
            field=models.TextField(blank=True, null=True),
        ),
    ]
