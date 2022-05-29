from unicodedata import name
from django.db import models
from django.forms import DateTimeField

class Pet(models.Model):
    SEX = [('M','Male'),('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank= True)
    description = models.TextField()
    sex = models.CharField(max_length=1,choices=SEX,blank=True)
    submit_date = models,DateTimeField()
    age = models.IntegerField(null=True)
    vaccination = models.ManyToManyField('Vaccine',blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

 