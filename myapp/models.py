from unittest.util import _MAX_LENGTH
from django.db import models
class student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    marks=models.FloatField()
    address=models.TextField()
    mob_no=models.IntegerField()
    email=models.EmailField()


