# Generated by Django 2.0.5 on 2018-05-27 14:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('haipumpfinder', '0011_auto_20180527_0843'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patient',
            new_name='Profile',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='profile',
        ),
    ]
