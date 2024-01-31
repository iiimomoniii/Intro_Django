from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

def index(request):
    #response only index.html 
    #return render(request,"index.html")

    #response index.html and objects
    # name = "Admin"
    # age = 10
    
    #response object in models
    all_person = Person.objects.all()
    return render(request,"index.html", {"all_person":all_person})

def about(request):
    return render(request,"about.html")

#Reponse with message
# def form(request):
#     return HttpResponse("From form")

#Reponse with Template
def form(request):
    return render(request,"form.html")