from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.models import Employee
from employee.serializer import EmployeeSerializer


@api_view(['GET', 'POST'])
def employees_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
# get the employee details from the employee entity    
@api_view(['GET'])
def employee_detail_per_employee(request, pk):
    try: 
        employees = Employee.objects.get(pk=pk) 
    except employees.DoesNotExist: 
        return JsonResponse({'message': 'The employee does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        serializer = EmployeeSerializer(employees) 
        return JsonResponse(serializer.data) 
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
 
    


 

    
    
    
    
# request delete data request to employee information  
@api_view(['DELETE'])
def request_delete_data(request, pk):
    try: 
        employees = Employee.objects.get(pk=pk) 
    except employees.DoesNotExist: 
        return JsonResponse({'message': 'The employee does not exist'}, status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'DELETE': 
        employees.delete() 
        return JsonResponse({'message': 'Employee was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    