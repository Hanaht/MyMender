# Generated by Django 4.1.7 on 2023-03-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
