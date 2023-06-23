# Generated by Django 4.1.7 on 2023-06-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(blank=True, max_length=20)),
            ],
        ),
    ]
