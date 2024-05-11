from django.shortcuts import render
from .models import Department,Doctor
from . forms import Bookingforms
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method =="POST":
         form = Bookingforms(request.POST)
         if form.is_valid():
              form.save()
              return render (request,'confirmation.html')

    form = Bookingforms()
    dict_form={
        'form':form
    }

    return render(request,'booking.html',dict_form)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept={
        'dept': Department.objects.all()
    }
    return render(request,'department.html',dict_dept)

def doctor(request):
     dict_dept={
        'doctor': Doctor.objects.all()
        }
     return render(request,'doctor.html',dict_dept)