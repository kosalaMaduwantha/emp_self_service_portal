from django.urls import re_path 
from Request.views import RequestDetailView, RequestListView, EmployeeRequestListView
 
 
urlpatterns = [ 
    re_path(r'^api/request/(?P<pk>[0-9]+)$', RequestDetailView.as_view(), name="get_request"),
    re_path(r'^api/requests/', RequestListView.as_view(), name="get_all_requests"),
    re_path(r'^api/employee/(?P<emp_key>[0-9]+)/requests$', EmployeeRequestListView.as_view(), name="get_employee_requests")
]