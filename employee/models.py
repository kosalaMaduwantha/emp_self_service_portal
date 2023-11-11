from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

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
    phone = models.CharField(validators=[phone_regex], max_length=15)
    emmergency_contact = models.CharField(validators=[phone_regex], max_length=15)
    
    
# these are the model

# here is another comment
    

    



