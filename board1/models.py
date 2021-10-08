from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ManyToManyField
from acc.models import User


# Create your models here.

class Board(models.Model):
    subject = CharField(max_length=100)
    writer = CharField(max_length=30)
    content =   TextField()
    likey = IntegerField()
    up = ManyToManyField(User)
    c_time = DateTimeField()

    def __str__(self):
        return self.subject

class Reply(models.Model):
    subject = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=100)
    comment = models.TextField()
    pic = models.ImageField()

