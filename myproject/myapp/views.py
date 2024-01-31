from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages
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
# def form(request):
#     return render(request,"form.html")

#Reponse Model
def form(request):
    if request.method == "POST":
        #display value
        name = request.POST["name"]
        age = request.POST["age"]

        #save
        person = Person.objects.create(
            name=name,
            age=age   
        )
        person.save()

        #message
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")    

        # redirect
        return redirect("/")
    else :
        return render(request,"form.html")
    

def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        #message
        messages.success(request,"บันทึกข้อมูลที่แก้ไขเรียบร้อย")    

        # redirect
        return redirect("/")
    else:
        #get data from person_id
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})
    
def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    #message
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    # redirect
    return redirect("/")