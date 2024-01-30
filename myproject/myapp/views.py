from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #response only index.html 
    #return render(request,"index.html")
    #response index.html and objects
    name = "Admin"
    age = 10
    return render(request,"index.html", {"firstName":name, "age":age})

def about(request):
    return render(request,"about.html")

#Reponse with message
# def form(request):
#     return HttpResponse("From form")

#Reponse with Template
def form(request):
    return render(request,"form.html")