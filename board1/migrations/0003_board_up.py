# Generated by Django 3.2.7 on 2021-09-30 06:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board1', '0002_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='up',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]