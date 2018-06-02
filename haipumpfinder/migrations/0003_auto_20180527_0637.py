# Generated by Django 2.0.5 on 2018-05-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haipumpfinder', '0002_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dx_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_treatment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='stage_now',
            field=models.CharField(choices=[('1', 'Stage 1'), ('2', 'Stage 2'), ('3', 'Stage 3'), ('4', 'Stage 4')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='patient',
            name='stage_at_dx',
            field=models.CharField(choices=[('1', 'Stage 1'), ('2', 'Stage 2'), ('3', 'Stage 3'), ('4', 'Stage 4')], default='1', max_length=2),
        ),
    ]
