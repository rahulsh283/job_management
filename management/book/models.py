from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length = 100)
    writer_name = models.CharField(max_length = 100)
    price  =  models.CharField(max_length = 100)
    vander_name = models.CharField(max_length = 100)
    purchase_date = models.CharField(max_length = 100)


class Student_info(models.Model):
    student_name = models.CharField(max_length = 100)
    student_class = models.CharField(max_length = 100)
    mother_name = models.CharField(max_length = 100)
    father_name =  models.CharField(max_length = 100)
    addmission_date = models.CharField(max_length = 100)
    email_address = models.CharField(max_length = 100)

