from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns=[
    path('mom/',mom,name='mom'),
    path('master/',master,name='master'),
]