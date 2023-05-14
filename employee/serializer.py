from rest_framework import serializers 
from employee.models import Employee, Department
 
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
 
class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = Employee
        fields = '__all__'
        
        
        
        
        
