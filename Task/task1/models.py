from unicodedata import name
from django.db import models

# Create your models here.
class task1(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    age = models.IntegerField()
    dob = models.DateField()

    def __str___(self):
        return self.name
