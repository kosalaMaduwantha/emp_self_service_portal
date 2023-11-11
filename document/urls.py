from django.urls import re_path 
from document.views import DocumentDetailView, DocumentListView, DocumentByEmployeeView, DocumentUploadView

urlpatterns = [
    re_path(r'^api/document/(?P<pk>[0-9]+)$', DocumentDetailView.as_view(), name="get_document"),
    re_path(r'^api/documents/', DocumentListView.as_view(), name="get_all_documents"),
    re_path(r'^api/employee/(?P<pk>[0-9]+)/documents$', DocumentByEmployeeView.as_view(), name="get_employee_documents"),
    re_path(r'^api/document/upload/', DocumentUploadView.as_view(), name="upload_document")
]
