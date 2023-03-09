from app2.views import *
from django.urls import path
app1_name='nothing'
urlpatterns=[
    path('second/',second,name='second'),
]