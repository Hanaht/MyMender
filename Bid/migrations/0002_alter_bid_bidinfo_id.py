# Generated by Django 4.1.7 on 2023-04-07 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidInfo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bid.bidinfo'),
        ),
    ]
