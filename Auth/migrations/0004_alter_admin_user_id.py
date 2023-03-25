# Generated by Django 4.1.7 on 2023-03-25 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_alter_admin_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='identification_number'),
        ),
    ]
