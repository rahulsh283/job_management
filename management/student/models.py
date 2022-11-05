from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.
class studentRegister(models.Model):
    roll_no = models.IntegerField(unique = True)
    student_name = models.CharField( max_length=100)
    class_name = models.CharField( max_length=100)
    section_name = models.CharField( max_length=100)
    mobile_no = models.CharField( max_length=100)
    email_address = models.CharField( max_length=100)
    gender = models.CharField(default="", max_length=100)
    course = models.CharField( max_length=100)
    year = models.CharField( max_length=100)
    semester = models.CharField( max_length=100)
    join_date = models.CharField( max_length=100)
    created_date = models.DateTimeField(default=timezone.now())