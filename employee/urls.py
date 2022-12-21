from django.urls import re_path 
from employee.views import employee_detail_per_employee, employees_list
 
 
urlpatterns = [ 
    re_path(r'^api/employee/(?P<pk>[0-9]+)$', employee_detail_per_employee, name="employee"),
    
]