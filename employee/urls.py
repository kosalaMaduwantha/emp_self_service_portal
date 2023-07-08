from django.urls import re_path 
from employee.views import EmployeeDetailView, EmployeeListView

 
 
urlpatterns = [ 
    re_path(r'^api/employee/(?P<pk>[0-9]+)$', EmployeeDetailView.as_view(), name="employee"),
    re_path(r'^api/employees/', EmployeeListView.as_view(), name="employees")
    
]