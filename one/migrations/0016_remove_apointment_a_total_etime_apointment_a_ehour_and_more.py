# Generated by Django 4.0.2 on 2022-05-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0015_rename_a_total_etime_cart_c_total_etime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apointment',
            name='a_total_etime',
        ),
        migrations.AddField(
            model_name='apointment',
            name='a_ehour',
            field=models.IntegerField(choices=[(0, 0), (1, '1 Hour'), (2, '2 Hour'), (3, '3 Hour'), (4, '4 Hour'), (5, '5 Hour'), (6, '6 Hour'), (7, '7 Hour')], null=True),
        ),
        migrations.AddField(
            model_name='apointment',
            name='a_emin',
            field=models.IntegerField(choices=[(10, '10 Minutes'), (20, '20 Minutes'), (30, '30 Minutes'), (40, '40 Minutes'), (50, '50 Minutes')], null=True),
        ),
    ]
