# Generated by Django 4.0.2 on 2022-03-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0006_alter_apointment_a_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apointment',
            name='a_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Done', 'Done'), ('Reject', 'Reject'), ('Absent', 'Absent')], default='Pending', max_length=20),
        ),
    ]