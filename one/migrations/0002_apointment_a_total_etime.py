# Generated by Django 4.0.2 on 2022-03-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apointment',
            name='a_total_etime',
            field=models.FloatField(null=True),
        ),
    ]
