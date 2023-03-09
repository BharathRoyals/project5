from app1.views import *
from django.urls import path 
app2_name='nothing'

urlpatterns=[
    path('first/',first,name='first'),
]