# Generated by Django 4.0.4 on 2022-04-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docappointment', '0005_appointment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]