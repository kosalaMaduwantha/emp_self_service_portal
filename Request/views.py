from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Request.models import Request
from Request.serializer import RequestSerializer

# Create your views here.


# request change data request to employee information  
@api_view(['POST'])
def employee_request_post(request):
    
    if request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    

@api_view(['GET'])
def get_employees_requests(request, emp_key):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        requests = Request.objects.filter(employee=emp_key) 
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)