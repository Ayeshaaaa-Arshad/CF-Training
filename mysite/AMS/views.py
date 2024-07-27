from .models import *
from django.shortcuts import render


def index_page(request):
    doctors = Doctor.objects.all()
    announcements=Announcement.objects.all()
    return render(request,'AMS/index.html',context={'Doctors' : doctors,
                                                    'announcements':announcements})

def edit_profile_page(request):
    return render(request,'AMS/edit_profile.html')

def book_appointment_page(request):
    return render(request,'AMS/book_appointment.html')

def treatments_page(request):
    return render(request,'AMS/treatments.html')

def login_page(request):
    return render(request,'AMS/login.html')

def signup_page(request):
    return render(request,'AMS/signup.html')