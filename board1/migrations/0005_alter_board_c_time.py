# Generated by Django 3.2.7 on 2021-10-04 05:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board1', '0004_board_c_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='c_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 4, 5, 33, 33, 100827, tzinfo=utc)),
        ),
    ]