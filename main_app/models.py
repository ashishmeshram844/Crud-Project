""" This file contain the model classes of employee """
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()

    def __str(self):
        return self.name
