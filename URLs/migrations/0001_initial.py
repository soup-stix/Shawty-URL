# Generated by Django 3.0 on 2022-11-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('short_url', models.TextField()),
                ('createTime', models.DateTimeField()),
            ],
        ),
    ]
