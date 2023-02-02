from django.urls import re_path 
from employee.views import EmployeeDetailView, employees_list
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
 
 
urlpatterns = [ 
    re_path(r'^api/employee/(?P<pk>[0-9]+)$', EmployeeDetailView.as_view(), name="employee")
    
]