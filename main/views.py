from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.


def home(requests):
    return HttpResponse('<b>Hah,hi bro</b>')



def check_age(request,age):

    if age >= 18:
        return HttpResponse('<b>Hi! You r not teen anymore</b>')
    
    elif age < 18:
        return HttpResponse('You r to young')
    
    else:
        return HttpResponse('enter tour age!')
    

def check_region(request,region):
    regions = ["Toshkent",'Andijon',"Farg‘ona","Namangan","Sirdaryo","Jizzax","Samarqand","Qashqadaryo", "Surxondaryo","Navoiy", "Buxoro","Xorazm","Qoraqalpog‘iston"]
    
    if region == 'Namangan':
            return HttpResponse('I am also from Namangan!')
       

    if   region in regions:
        return HttpResponse(f'<b>Oh, {region} is really good!</b>')

    else:
        return HttpResponse('Please enter region,which located in Uzbekistan!')
    
    
    
    