# Generated by Django 4.0.2 on 2022-03-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_apointment_a_total_etime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apointment',
            name='a_total_etime',
            field=models.IntegerField(null=True),
        ),
    ]
