# Generated by Django 2.0.5 on 2018-05-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haipumpfinder', '0005_auto_20180527_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='msi_status',
        ),
        migrations.AlterField(
            model_name='profile',
            name='stage_at_dx',
            field=models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='stage_now',
            field=models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV')], default='1', max_length=20),
        ),
    ]
