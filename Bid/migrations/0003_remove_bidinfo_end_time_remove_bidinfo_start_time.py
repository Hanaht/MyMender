# Generated by Django 4.1.7 on 2023-04-07 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bid', '0002_alter_bid_bidinfo_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidinfo',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='bidinfo',
            name='start_time',
        ),
    ]