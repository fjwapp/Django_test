from django.db import models
from mongoengine import *
#ORM
from mongoengine import connect
connect('wbsite',host='localhost',port=27017)



class ArtiInfo(Document):
    url = StringField()
    address = StringField()
    deal_number = StringField()
    title = StringField()
    price = StringField()
    person_look_count = StringField()

    meta = {'collection':'wbsite_item'}


# Create your models here.
class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    content_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=300)
    comment = models.TextField()
    time = models.CharField(null=True, blank=True, max_length=50)
    def __str__(self):
        return self.name