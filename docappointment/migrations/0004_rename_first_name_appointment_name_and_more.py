# Generated by Django 4.0.4 on 2022-04-21 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docappointment', '0003_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='last_name',
        ),
    ]
