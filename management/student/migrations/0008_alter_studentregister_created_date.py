# Generated by Django 4.1.1 on 2022-10-11 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_studentregister_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 8, 9, 46, 160490, tzinfo=datetime.timezone.utc)),
        ),
    ]
