# Generated by Django 4.1.7 on 2023-03-25 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, verbose_name='email address')),
                ('identification_number', models.BigIntegerField(unique=True)),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
