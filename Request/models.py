from django.db import models
from employee.models import Employee

# Create your models here.

class Request(models.Model):
    request_type = models.CharField(max_length=40)
    request_name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

