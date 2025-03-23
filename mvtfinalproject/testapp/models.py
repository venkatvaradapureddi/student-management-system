from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.IntegerField()
    subject = models.CharField(max_length=30)
    dob= models.DateField()
    phoneno = models.BigIntegerField()
