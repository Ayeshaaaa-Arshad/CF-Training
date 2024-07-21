from django.shortcuts import render

def index_page(request):
    return render(request,'AMS/index.html')

def edit_profile_page(request):
    return render(request,'AMS/edit_profile.html')

def book_appointment_page(request):
    return render(request,'AMS/book_appointment.html')

def prev_treatment_page(request):
    return render(request,'AMS/prev_treatment.html')

def login_singup_page(request):
    return render(request,'AMS/login_signup.html')