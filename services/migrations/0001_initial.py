# Generated by Django 4.1.7 on 2023-06-02 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('admin_ID', models.ManyToManyField(to='Auth.admin')),
                ('dep_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.department')),
            ],
        ),
        migrations.CreateModel(
            name='general_requirment',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('service_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
    ]
