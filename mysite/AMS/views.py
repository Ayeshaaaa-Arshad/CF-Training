from typing import Any
from .models import *
from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView


# Home page Displaying List of all doctors Along with the announcments and Latest Treatment of logged in Patient
class IndexPageView(ListView):
    template_name = 'AMS/index.html'
    context_object_name = 'Doctors'
    queryset = Doctor.objects.all()

    # updating the context data and adding announcements in it 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Announcements'] = Announcement.objects.all()
        context['Treatment'] = Treatments.objects.first()
        return context

# Template View to Render Edit Profile Page of User
class EditProfileView(TemplateView):
    template_name='AMS/edit_profile.html'


# Detail View For displaying each Doctor for booking Appointment
class BookAppointmentView(DetailView):
    template_name = 'AMS/book_appointment.html'
    model = Doctor
    context_object_name='Doctor'

# List View For Each patient's All Treatments List
class TreatmentView(ListView):
    template_name = 'AMS/treatments.html'
    context_object_name = 'Treatments'
    queryset = Treatments.objects.all()

# Login Page 
def login_page(request):
    return render(request,'AMS/login.html')

# Signup Page
def signup_page(request):
    return render(request,'AMS/signup.html')