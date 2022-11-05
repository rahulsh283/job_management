from django.db import models

# Create your models here.
class Employee(models.Model):
    company_name = models.CharField(max_length = 100) 
    official_email = models.CharField(max_length = 100)
    mobile_number = models.CharField(max_length = 100)
    Contact_person_name = models.CharField(max_length = 100)
    pin_code = models.CharField(max_length = 100)
    company_type = models.CharField(max_length = 100)
    GSTIN = models.CharField(max_length = 100)
    password =models.CharField(default="" ,max_length = 100) 