# Generated by Django 4.1.7 on 2023-03-28 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0002_customer'),
        ('services', '0002_admin_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('app_date', models.DateField()),
                ('status', models.CharField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('admin_service_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.admin_services')),
                ('customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.customer')),
                ('dep_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.department')),
            ],
        ),
    ]
