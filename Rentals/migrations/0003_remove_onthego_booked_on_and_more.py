# Generated by Django 4.1.2 on 2022-10-18 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rentals', '0002_rename_booked_on_onthego_booked_on_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onthego',
            name='Booked_on',
        ),
        migrations.RemoveField(
            model_name='scheduleride',
            name='Booked_on',
        ),
    ]
