from django.shortcuts import render
from .models import *

def index_page(request):
    doctors = Doctor.objects.all()
    announcements=Announcement.objects.all()
    return render(request,'AMS/index.html',context={'Doctors' : doctors,
                                                    'announcements':announcements})

def edit_profile_page(request):
    return render(request,'AMS/edit_profile.html')

def book_appointment_page(request):
    return render(request,'AMS/book_appointment.html')

def prev_treatment_page(request):
    return render(request,'AMS/prev_treatment.html')

def login_singup_page(request):
    return render(request,'AMS/login_signup.html')