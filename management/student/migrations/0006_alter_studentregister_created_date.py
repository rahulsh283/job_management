# Generated by Django 4.1.1 on 2022-10-03 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_studentregister_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 19, 22, 1, 77887, tzinfo=datetime.timezone.utc)),
        ),
    ]
