from django.db import models

# Create your models here.

# model for the user authentication + registration

class Department(models.Model):
    department_name = models.CharField(max_length=20)

class Employee(models.Model):
    legal_first_name = models.CharField(max_length=100)
    legal_last_name = models.CharField(max_length=100)
    pref_first_name = models.CharField(max_length=100)
    pref_last_name = models.CharField(max_length=100)
    NIC = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    country_of_birth = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    citizenship_status = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    
    
# these are the model

# here is another comment
    

    



