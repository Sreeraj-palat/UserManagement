from distutils.command.upload import upload
from email.mime import image
import imp
from django.db import models
import datetime
import os

# Create your models here.

def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/',filename)


class Item(models.Model):
    name = models.TextField(max_length=100)
    price = models.TextField(max_length=10)
    description = models.TextField(max_length=250, null=True)
    image = models.ImageField(null=True,blank=True,upload_to = "images/")