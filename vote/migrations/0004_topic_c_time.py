# Generated by Django 3.2.7 on 2021-10-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_alter_choice_cuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='c_time',
            field=models.DateTimeField(null=True),
        ),
    ]