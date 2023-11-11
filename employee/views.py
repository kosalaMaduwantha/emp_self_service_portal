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
from self_service_portal.utilities.logger import Logger

logger = Logger(__name__)

# get all the employees as a list
class EmployeeListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            logger.info("get all employees")
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
        except Exception as e:
            logger.error("an error occured {}".format(e))
            return Response({"message":"an error occured {}".format(e)})
        return Response(serializer.data)

# get specific employee details
class EmployeeDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return Response({'message': 'The employee does not exist', 'error':str(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return Response({'message': 'The employee does not exist', 'error':str(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



    
    