# Generated by Django 4.0.2 on 2022-03-23 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0008_rename_apointment_appointments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='appointments',
            new_name='apointment',
        ),
    ]