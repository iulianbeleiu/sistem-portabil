# Generated by Django 2.2.12 on 2020-06-01 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0007_auto_20200601_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='user_pacient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_pacient', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
