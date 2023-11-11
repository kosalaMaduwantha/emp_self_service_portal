from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from self_service_portal.utilities.logger import Logger
from document.models import Document
from document.serializer import DocumentSerializer, DocumentUploadSerializer
from django.core.exceptions import ObjectDoesNotExist
from employee.models import Employee
import os
import datetime

# Create your views here.

# create a logger instance
logger = Logger(__name__)

# get the relative path of the data directory
data_path = os.path.join('document','data')

# get all the documents as a list
class DocumentListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            documents = Document.objects.all()
            serializer = DocumentSerializer(documents, many=True)
        except Exception as e:
            logger.error("an error occured {}".format(e))
            return Response({"message":"an error occured {}".format(e)})
        return Response(serializer.data)

# get post, delete specific document details
class DocumentDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = DocumentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except Exception as e:
            logger.error("an error occured {}".format(e))
            return Response({"message":"an error occured {}".format(e)})
        return Response(serializer.data)

    def get(self, request, pk):
        try:
            document = Document.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return Response({'message': 'The document does not exist', 'error':str(e)}, status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        try:
            document = Document.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return Response({'message': 'The document does not exist', 'error':str(e)}, status=status.HTTP_404_NOT_FOUND)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# get documents by employee id
class DocumentByEmployeeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            documents = Document.objects.filter(employee=pk)
            serializer = DocumentSerializer(documents, many=True)
        except Exception as e:
            logger.error("an error occured {}".format(e))
            return Response({"message":"an error occured {}".format(e)})
        return Response(serializer.data)
    
class DocumentUploadView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            # get the file from the request
            file = request.FILES['file']
            file_name = file.name
            # write data to the file
            os.makedirs(data_path, exist_ok=True)
            with open(os.path.join(data_path,file_name), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            uploaded_date = datetime.datetime.utcnow()
            # get employee by id
            employee = Employee.objects.get(pk=request.data['employee'])
            # create a document object
            document = Document.objects.create(
                name_doc=file_name,
                description=request.data['description'],
                uploaded_date=uploaded_date,
                updated_date=uploaded_date,
                document_category=request.data['document_category'],
                doc_link=os.path.join(data_path,file_name),
                employee=employee
            )
            serializer = DocumentUploadSerializer(document)
        except Exception as e:
            logger.error("an error occured {}".format(e))
            return Response({"message":"an error occured {}".format(e)})
        return Response(serializer.data)                
            
            
            
            
    
    
