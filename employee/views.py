# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.models import Employee
from employee.serializer import EmployeeSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# @api_view(['GET', 'POST'])
# def employees_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# get all the employees as a list
class EmployeeListView(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        try:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
        except Exception as e:
            return Response({"message":"an error occured {}".format(e)})
        return Response(serializer.data)

# class bases view refactering
class EmployeeDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return Response({'message': 'The employee does not exist', 'error':str(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    

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
    
# get the employee details from the employee entity    
# @api_view(['GET'])
# def employee_detail_per_employee(request, pk):
#     try: 
#         employees = Employee.objects.get(pk=pk) 
#     except employees.DoesNotExist: 
#         return JsonResponse({'message': 'The employee does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
#     if request.method == 'GET': 
#         serializer = EmployeeSerializer(employees) 
#         return JsonResponse(serializer.data) 
#     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    
    