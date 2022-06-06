from distutils.command.upload import upload
from pyexpat import model
from tkinter import Image
from django.db import models

# Create your models here.
class Job(models.Model):

    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=200)
