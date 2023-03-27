# Generated by Django 4.1.7 on 2023-03-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BidInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=39)),
                ('description', models.TextField(max_length=200)),
                ('initial_price', models.FloatField()),
                ('end_time', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('winner', models.TextField(max_length=20)),
                ('final_price', models.FloatField()),
                ('numberOfExperience', models.IntegerField()),
            ],
        ),
    ]