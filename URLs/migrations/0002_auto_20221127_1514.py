# Generated by Django 3.0 on 2022-11-27 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
