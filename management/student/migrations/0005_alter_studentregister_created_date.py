# Generated by Django 4.1.1 on 2022-10-03 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_studentregister_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 18, 31, 46, 577848, tzinfo=datetime.timezone.utc)),
        ),
    ]
