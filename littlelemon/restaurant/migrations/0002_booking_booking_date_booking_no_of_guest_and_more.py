# Generated by Django 5.1.7 on 2025-03-12 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guest',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(null=True),
        ),
    ]
