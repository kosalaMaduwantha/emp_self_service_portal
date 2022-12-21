from django.urls import re_path 
from Request.views import employee_request_post, get_employees_requests
 
 
urlpatterns = [ 
    re_path(r'^api/request/(?P<emp_key>[0-9]+)$', get_employees_requests, name="request_get"),
    re_path(r'^api/request/', employee_request_post, name="request_post")
]