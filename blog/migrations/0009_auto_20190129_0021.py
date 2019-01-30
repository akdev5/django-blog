# Generated by Django 2.1.4 on 2019-01-29 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190129_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 29, 0, 21, 39, 296873)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply_to',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 29, 0, 21, 39, 296279)),
        ),
    ]
