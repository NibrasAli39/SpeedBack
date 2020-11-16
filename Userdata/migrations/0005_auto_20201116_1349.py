# Generated by Django 2.1.5 on 2020-11-16 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Userdata', '0004_driverdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='addressDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('city', models.CharField(blank=True, max_length=300, null=True)),
                ('street_address', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(blank=True, max_length=300, null=True)),
                ('pickup_location', models.CharField(blank=True, max_length=300, null=True)),
                ('dropoff_location', models.CharField(blank=True, max_length=300, null=True)),
                ('dropoff_lat', models.FloatField(default=0)),
                ('dropoff_lon', models.FloatField(default=0)),
                ('customer_name', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_number', models.CharField(blank=True, max_length=300, null=True)),
                ('order_status', models.CharField(blank=True, max_length=300, null=True)),
                ('order_price', models.FloatField(default=0)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='driverdetails',
            name='mobile_number',
            field=models.IntegerField(default=0),
        ),
    ]
