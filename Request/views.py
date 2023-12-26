from django.shortcuts import render

# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from Request.models import Request
from Request.serializer import RequestSerializer
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
# Create your views here.

# get all the requests as a list
class RequestListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            requests = Request.objects.all()
            serializer = RequestSerializer(requests, many=True)
        except Exception as e:
            return Response({"message":"an error occured {}".format(e)})
        return Response(serializer.data)
    
    
# get specific request details
class RequestDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        try:
            serializer = RequestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except Exception as e:
            return Response({"message":"an error occured {}".format(e)})
        return Response(serializer.data)
    
    def get(self, request, pk):
        try:
            request = Request.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return Response({'message': 'The request does not exist', 'error':str(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = RequestSerializer(request)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        try:
            request = Request.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return Response({'message': 'The request does not exist', 'error':str(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = RequestSerializer(request, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            request = Request.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return Response({'message': 'The request does not exist', 'error':str(e)}, status=status.HTTP_404_NOT_FOUND)
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
# get request data by employee id
class EmployeeRequestListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, emp_key):
        try:
            requests = Request.objects.filter(employee=emp_key)
            serializer = RequestSerializer(requests, many=True)
        except Exception as e:
            return Response({"message":"an error occured {}".format(e)})
        return Response(serializer.data)
    
    

    
