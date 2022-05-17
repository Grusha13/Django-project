from turtle import title
from django.db import models

# Models describes the database objects eg: tables, fields etc

class Book(models.Model):
    title =  models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
