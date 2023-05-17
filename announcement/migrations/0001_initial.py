# Generated by Django 4.1.7 on 2023-05-03 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcement',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=5000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('admin_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.admin')),
                ('dep_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.department')),
            ],
        ),
    ]
