# Generated by Django 4.0.4 on 2022-04-21 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docappointment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
