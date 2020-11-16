# Generated by Django 3.1.2 on 2020-10-30 16:41

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
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.CharField(blank=True, max_length=50000, null=True)),
                ('attachments', models.FileField(blank=True, null=True, upload_to='content_images')),
                ('paid_status', models.CharField(blank=True, choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.IntegerField(default=0)),
                ('date_generated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('user_name', models.CharField(max_length=300)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_images')),
                ('date_generated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(blank=True, choices=[('shop', 'shop'), ('bitcoin', 'bitcoin')], max_length=300, null=True)),
                ('current_balance', models.IntegerField(default=0, max_length=200)),
                ('paid_status', models.CharField(blank=True, choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], max_length=300, null=True)),
                ('date_generated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
