# Generated by Django 4.1.7 on 2023-06-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
        migrations.AddField(
            model_name='appointment',
            name='ApprovalStatus',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
