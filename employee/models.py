from django.db import models

# Create your models here.

# model for the user authentication + registration

class Department(models.Model):
    department_name = models.CharField(max_length=20)

class Employee(models.Model):
    legal_first_name = models.CharField(max_length=30)
    legal_last_name = models.CharField(max_length=30)
    pref_first_name = models.CharField(max_length=30)
    pref_last_name = models.CharField(max_length=30)
    NIC = models.CharField(max_length=15)
    email = models.EmailField(unique=True, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    country_of_birth = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=10)
    ethnicity = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    citizenship_status = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    
    
# these are the model

# here is another comment
    

    



