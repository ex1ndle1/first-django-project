from django.contrib import admin
from django.urls import path

from .views import home,check_age,check_region

urlpatterns = [
 
    path('home/',home)
    ,
    path('check_age/<int:age>/',check_age),
    path('check_region/<str:region>',check_region)
]
 