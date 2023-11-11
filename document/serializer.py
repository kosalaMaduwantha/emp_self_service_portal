from rest_framework import serializers 
from document.models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        
class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['name_doc','description','uploaded_date','updated_date','document_category','doc_link','employee']