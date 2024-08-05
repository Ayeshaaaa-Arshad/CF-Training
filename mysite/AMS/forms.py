from django import forms
from django.utils import timezone
from django.shortcuts import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Feedback,CustomUser,Patient,Doctor,Appointment,Announcement,Treatment,Prescription

# Signup Form inherited from UserCreationForm as we want to add some extra fields 
class SignupForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))

    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name", "password1", "password2")

# Login Form inherited from AuthenticationForm as we want to add some extra fields 
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = get_user_model()
        fields = ("username", "password")

#Feedback Form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Rate from 1 to 5'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your feedback'}),
        }

#CustomUserForm
class CustomUserForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=[
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
        ('Receptionist', 'Receptionist')
    ], required=True)
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email', 'image', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)  # Hash the password
        if commit:
            user.save()

             # Assign user to the selected group
            user_type = self.cleaned_data.get('user_type')
            group = Group.objects.get(name=user_type)
            user.groups.add(group)
        return user

#Patient Form
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['age']

#Doctor Form
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['designation']

#AppointmentForm
class AppointmentForm(forms.ModelForm):
    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'disease', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'disease': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            if user.groups.filter(name='Patient').exists():
                self.fields['patient'].queryset = Patient.objects.filter(user=user)
                self.fields['patient'].initial = user.patient_profile
                self.fields['doctor'].queryset = Doctor.objects.all()
                
            elif user.groups.filter(name='Admin').exists() or user.groups.filter(name='Receptionist').exists():
                self.fields['patient'].queryset = Patient.objects.all()
                self.fields['doctor'].queryset = Doctor.objects.all()
            else:
                # Non-admin and non-doctor users see no patients and doctors
                self.fields['patient'].queryset = Patient.objects.none()
                self.fields['doctor'].queryset = Doctor.objects.none()

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data.get('appointment_date')
        now = timezone.now()

        if appointment_date and appointment_date < now:
            self.add_error('appointment_date', "The appointment date cannot be in the past.")

        return appointment_date
    
#AnnouncementForm
class AnnouncementForm(forms.ModelForm):
    creator = forms.ModelChoiceField(queryset=CustomUser.objects.none(), required=False)  

    class Meta:
        model = Announcement
        fields = ['title', 'description', 'creator']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['creator'].queryset = CustomUser.objects.filter(id=user.id)
            self.fields['creator'].initial = user

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['patient', 'doctor', 'remarks']
        widgets = {
            'remarks': forms.Textarea(attrs={'class': 'form-control'}),
           'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            if user.groups.filter(name='Admin').exists():
                # Admin can see all patients and doctors
                self.fields['patient'].queryset = Patient.objects.all()
                self.fields['doctor'].queryset = Doctor.objects.all()
            elif user.groups.filter(name='Doctor').exists():
                # Logged-in doctor can see only their own patients
                doctor = user.doctor_profile
                self.fields['patient'].queryset = Patient.objects.filter(
                    id__in=Appointment.objects.filter(doctor=doctor).values_list('patient_id', flat=True)
                )
                self.fields['doctor'].queryset = Doctor.objects.filter(id=doctor.id)
            else:
                # Non-admin and non-doctor users see no patients and doctors
                self.fields['patient'].queryset = Patient.objects.none()
                self.fields['doctor'].queryset = Doctor.objects.none()

        # Debug output
        print(f"User: {user}")
        print(f"Patient queryset: {self.fields['patient'].queryset.query}")
        print(f"Doctor queryset: {self.fields['doctor'].queryset.query}")

#PrescriptionForm
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['details']

#EditProfileForm with custom fields
class EditProfileForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'image']

    def __init__(self, *args, **kwargs):
        # Extract the user object from kwargs
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # role-specific fields if the user is a patient, doctor, 
        if user:
            if user.groups.filter(name='Patient').exists():
                self.fields['age'] = forms.IntegerField(
                    initial=user.patient_profile.age,
                    widget=forms.NumberInput(attrs={'placeholder': 'Age'})
                )
            elif user.groups.filter(name='Doctor').exists():
                self.fields['designation'] = forms.CharField(
                    initial=user.doctor_profile.designation,
                    widget=forms.TextInput(attrs={'placeholder': 'Designation'})
                )

    def save(self, commit=True):
        user = super().save(commit=False)
        # Save custom fields
        if commit:
            user.save()
        # Update role-specific details if applicable
        if user.groups.filter(name='Patient').exists():
            patient = user.patient_profile
            if 'age' in self.cleaned_data:
                patient.age = self.cleaned_data['age']
                patient.save()
        elif user.groups.filter(name='Doctor').exists():
            doctor = user.doctor_profile
            if 'designation' in self.cleaned_data:
                doctor.designation = self.cleaned_data['designation']
                doctor.save()
       
        return user
    