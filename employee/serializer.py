from rest_framework import serializers 
from employee.models import Employee
 
 
class EmployeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employee
        fields = ('legal_first_name',
                  'legal_last_name',
                  'pref_first_name',
                  'pref_last_name',
                  'NIC',
                  'age',
                  'email',
                  'gender',
                  'dob',
                  'country_of_birth',
                  'marital_status',
                  'ethnicity',
                  'nationality',
                  'citizenship_status',
                  'department',
                  'phone',
                  'address')
        
        
        
        
        
