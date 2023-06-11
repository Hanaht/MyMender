# Generated by Django 4.1.7 on 2023-06-10 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deliverd_on', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True, max_length=500)),
                ('phone_number', models.TextField(blank=True, max_length=500)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.customer')),
            ],
        ),
    ]
