from django.db import models

# Create your models here.




class School(models.Model):
    scname=models.CharField(max_length=100)
    scprincpal=models.CharField(max_length=100)
    sclocation=models.CharField(max_length=100)


class Student(models.Model):
    sname=models.CharField(max_length=100)
    sag=models.IntegerField(max_length=100)
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='Rahul')