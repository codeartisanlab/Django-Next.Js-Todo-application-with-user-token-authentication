# Generated by Django 5.0.3 on 2024-04-09 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 9, 23, 16, 16, 321880)),
        ),
    ]
