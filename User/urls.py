from django.urls import path
#from User.views import CustomUserCreate
from django.urls import re_path 


from django.urls import path
from .views import UserCreate, LoginView, LogoutView

urlpatterns = [
    path('api/signup/', UserCreate.as_view(), name='account-create'),
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    # other urls...
]