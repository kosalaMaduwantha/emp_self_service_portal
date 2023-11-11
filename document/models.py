from django.db import models
from employee.models import Employee

# Create your models here.

class Document(models.Model):
    name_doc = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    uploaded_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    document_category = models.CharField(max_length=40)
    doc_link = models.CharField(max_length=300)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    
# hi menna change ekak
