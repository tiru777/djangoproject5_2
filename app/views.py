from django.shortcuts import render
from app.models import *
from app.forms import EmployeeForm
from django.http import HttpResponseRedirect
def home(requests):
    return render(requests,"home.html")

def list_employee(requests):
    data = Employee.objects.all() # all data fetch from database
    data_check = Employee.objects.all().count() # all data fetch from database
    print(data_check)
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

def delete_employee(requests,id):
    data = Employee.objects.get(id=id) # we can get specific data of object
    data.delete()
    return HttpResponseRedirect("/list")

# ORM
def list_employe(requests):
    # READ ALL
    # all data fetch from database
    data_all = Employee.objects.all()
    # count
    data_all_count = Employee.objects.all().count()
    # order by
    data_order = Employee.objects.all().order_by('age')# ASC
    data_order_dsc = Employee.objects.all().order_by('-age')# ASC
    # index
    data_second_index = Employee.objects.all()[2]

    # filter
    data = Employee.objects.filter(age__gt=20)
    # gt ==>greter than
    # lt ==>less than
    #gte,lte

    daa = Employee.objects.filter(first_name__startswith="p",age__gt=20)

    # GET Specific
    # get specific person==prakash
    data = Employee.objects.get(first_name="prakash")
    print(data)

    # update specific object
    data_up = Employee.objects.get(first_name="prakash")
    data_up.second_name = "daram"
    data_up.age=20
    data_up.save()

    # delete all
    data = Employee.objects.all().delete() # delete all

    # specific object delete
    data = Employee.objects.get(id=2)
    data.delete()

    # Create
    data=Employee.objects.create(name='thirumala',salary=1000,address='reddy vari palli',age=20)
    data.save()
