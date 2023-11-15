from django.shortcuts import render
from app.models import *
from app.forms import EmployeeForm
from django.http import HttpResponseRedirect
def home(requests):
    return render(requests,"home.html")

def list_employee(requests):
    data = Employee.objects.all() # all data fetch from database
    return render(requests,"list_employee.html",context={"data":data})

def create_employee(requests):
    form = EmployeeForm(requests.POST)
    if requests.method =="POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/list")

    return render(requests,"create_employee.html",context={"form":form})

def detailed_employee(requests,id):
    data = Employee.objects.get(id=id) # we can get specific data of object
    return render(requests,"detailed_employee.html",context={"data":data})

def update_employee(requests,id):
    data_employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=data_employee)
    if requests.method =="POST":
        form = EmployeeForm(requests.POST, instance=data_employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/list")

    return render(requests,"update_employee.html",context={"form":form})

