# Generated by Django 3.2.13 on 2022-06-16 06:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 6, 19, 30, 151737, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
