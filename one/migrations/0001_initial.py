# Generated by Django 4.0.2 on 2022-03-21 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sal_name', models.CharField(max_length=30, null=True)),
                ('sal_phn_no', models.CharField(max_length=13, null=True)),
                ('sal_adr', models.CharField(max_length=30, null=True)),
                ('sal_otime', models.TimeField()),
                ('sal_ctime', models.TimeField()),
                ('sal_about', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Both', 'Both'), ('Ladies', 'Ladies'), ('Gentleman', 'Gentleman')], max_length=15, null=True)),
                ('sal_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20, null=True)),
                ('s_price', models.FloatField(null=True)),
                ('s_about', models.TextField(blank=True, null=True)),
                ('s_emin', models.IntegerField(choices=[(10, 10), (20, 20), (30, 30), (40, 40), (50, 50)], null=True)),
                ('s_ehour', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('s_salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='one.salon')),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cl_phn_no', models.CharField(max_length=13, null=True)),
                ('cl_name', models.CharField(max_length=20, null=True)),
                ('cl_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='apointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_status', models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Done', 'Done'), ('Reject', 'Reject')], default='Pending', max_length=20)),
                ('a_total_price', models.FloatField(null=True)),
                ('a_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='one.client')),
                ('a_salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='one.salon')),
                ('a_service', models.ManyToManyField(to='one.services')),
            ],
            options={
                'unique_together': {('a_salon', 'a_client')},
            },
        ),
    ]