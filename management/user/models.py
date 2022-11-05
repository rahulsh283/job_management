
from asyncio.windows_events import NULL
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
import os



class Country(models.Model):
    name = models.CharField(max_length=100)
    sortname = models.CharField(max_length=100)

class States(models.Model):
    name = models.CharField(max_length = 100)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)


def get_upload_to(instance, filename):
    return 'upload/'+ str(instance.id)+ '/'+filename

# Create your models here.
class Frontend(models.Model):
    first_name = models.CharField( max_length=90)
    last_name = models.CharField( max_length=90)
    gender = models.CharField(default="", max_length=90)
    mobile_number = models.CharField(default='', max_length=100)
    email_address = models.CharField( max_length=30,unique=True)
    work_status = models.CharField(default="", max_length = 100)
    upload_resume = models.FileField(default=NULL, upload_to=get_upload_to)
    country_id = models.ForeignKey(Country, default="", on_delete=models.CASCADE)
    state_id = models.ForeignKey(States, default="", on_delete=models.CASCADE) 
    password = models.CharField(default='', max_length=200)
    added_date = models.DateTimeField(default=timezone.now())
    


class ContactUs(models.Model):
    email_addres = models.CharField( max_length=30)
    subject = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    added_date = models.DateTimeField(default=timezone.now()) 


