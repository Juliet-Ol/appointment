# Generated by Django 4.0.4 on 2022-04-21 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('docappointment', '0004_rename_first_name_appointment_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
