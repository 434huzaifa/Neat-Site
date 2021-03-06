# Generated by Django 4.0.2 on 2022-03-26 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0009_rename_appointments_apointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apointment',
            name='a_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='one.client'),
        ),
        migrations.AlterField(
            model_name='apointment',
            name='a_salon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='one.salon'),
        ),
        migrations.AlterField(
            model_name='services',
            name='s_ehour',
            field=models.IntegerField(choices=[(0, 0), (1, '1 Hour'), (2, '2 Hour'), (3, '3 Hour'), (4, '4 Hour'), (5, '5 Hour'), (6, '6 Hour'), (7, '7 Hour')], null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='s_emin',
            field=models.IntegerField(choices=[(10, '10 Minutes'), (20, '20 Minutes'), (30, '30 Minutes'), (40, '40 Minutes'), (50, '50 Minutes')], null=True),
        ),
    ]
