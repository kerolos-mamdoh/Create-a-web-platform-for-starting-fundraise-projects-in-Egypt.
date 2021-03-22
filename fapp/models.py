from django.db import models

# Create your models here.
from tagging.models import Tag


class addproject(models.Model):
    tittle=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    total_target=models.IntegerField()
    uploadimg = models.ImageField(upload_to='uploads/')
    tags = models.ManyToManyField(Tag ,related_name='photos',null=True)
    startdate= models.DateTimeField(auto_now_add=True)
    edndate = models.DateTimeField(auto_now_add=False)
    id_user=models.IntegerField(null=True)

class comment_project(models.Model):
    project_id=models.IntegerField()
    comment=models.CharField(max_length=100)

class Person(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

class donnate(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    project_id=models.IntegerField()