from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.


def home(requests):
    return HttpResponse('<b>Hah,hi bro</b>')



def check_age(request):
    age = request.GET.get("age")

    if age >= 18:
        return HttpResponse('<b>Hi! You r not teen anymore</b>')
    
    elif age < 18:
        return HttpResponse('You r to young')
    
    else:
        return HttpResponse('enter tour age!')
    

