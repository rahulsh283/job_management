# Generated by Django 4.1.1 on 2022-10-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
