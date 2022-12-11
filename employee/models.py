from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=20)

class Employee(models.Model):
    legal_first_name = models.CharField(max_length=30)
    legal_last_name = models.CharField(max_length=30)
    pref_first_name = models.CharField(max_length=30)
    pref_last_name = models.CharField(max_length=30)
    NIC = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    country_of_birth = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=10)
    ethnicity = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    citizenship_status = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    



