from django.db import models

# Create your models here.
class User(models.Model):
    roll = models.TextField()
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.TextField(max_length=30)
    class Meta:
        db_table="login"


class final_class(models.Model):
    roll_no=models.CharField(max_length=10)
    branch=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    section=models.IntegerField()
    mid=models.IntegerField()
    sub_code=models.CharField(max_length=20)
    marks=models.IntegerField()
    class Meta:
        db_table='mid'