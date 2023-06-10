# Generated by Django 4.1.7 on 2023-06-10 06:23

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
            name='Bid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, max_length=200)),
                ('description', models.TextField(max_length=200, null=True)),
                ('initial_price', models.FloatField()),
                ('start_time', models.DateTimeField(null=True)),
                ('minimum_numberOfExperience', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BidCatagory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('catagoryName', models.TextField(max_length=200)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Commpetition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, max_length=200)),
                ('final_price', models.FloatField()),
                ('winner', models.TextField(max_length=20)),
                ('numberOfExperience', models.IntegerField()),
                ('bid_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bid.bid')),
                ('winner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_Id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='catagory_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bid.bidcatagory'),
        ),
    ]
