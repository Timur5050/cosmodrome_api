# Generated by Django 5.0.7 on 2024-07-24 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangar', '0002_alter_racketflight_flight_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
