# Generated by Django 4.1.7 on 2023-06-10 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('app_date', models.DateField()),
                ('status', models.BooleanField()),
                ('pending', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.customer')),
                ('dep_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.department')),
                ('service_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
    ]