# Generated by Django 4.1.7 on 2023-05-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='phone_number',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
