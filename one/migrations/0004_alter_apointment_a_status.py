# Generated by Django 4.0.2 on 2022-03-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0003_alter_apointment_a_total_etime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apointment',
            name='a_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Done', 'Done'), ('Reject', 'Reject')], max_length=20),
        ),
    ]