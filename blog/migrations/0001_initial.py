# Generated by Django 3.2.13 on 2022-06-12 08:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(default=datetime.datetime(2022, 6, 12, 8, 19, 23, 56900, tzinfo=utc), verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(verbose_name='修改时间')),
                ('abstract', models.CharField(blank=True, max_length=500, verbose_name='摘要')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='分类')),
                ('tag', models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
