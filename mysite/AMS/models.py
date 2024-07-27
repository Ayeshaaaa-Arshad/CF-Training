from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_image_file_extension
from django.core.exceptions import ValidationError
from .CustomManager import AppointmentManager,UserManager
    

class CustomUser(AbstractUser):
    GENDER_TYPE = [
        ("F","Female"),
        ("M","Male"),
        ("O","Other")
    ]

    gender = models.CharField(max_length=1, choices=GENDER_TYPE)
    image = models.ImageField(upload_to='profile/images',verbose_name='Profile Image',blank=True,null=True,validators=[validate_image_file_extension])
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email' # setting Email for log in
    REQUIRED_FIELDS = []

    objects = UserManager()
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Patient(models.Model):
    age = models.PositiveIntegerField()
    user = models.OneToOneField(CustomUser,related_name='patient_profile',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"Patient: {self.user.first_name} {self.user.first_name}, Age: {self.age}"

class Doctor(models.Model):
    designation = models.CharField(max_length=255)
    user = models.OneToOneField(CustomUser,related_name='doctor_profile',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return f"Doctor: {self.user.first_name} {self.user.first_name}, Designation: {self.designation}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.BooleanField()

    objects = AppointmentManager() # Custom Manager for Appointments

    def __str__(self):
        return f"Appointment: {self.patient} with {self.doctor} on {self.date}"
    
    def clean(self):
        # Call the parent class's clean method
        super().clean()

        # Check if the patient and doctor are the same user
        if self.patient.user == self.doctor.user:
            raise ValidationError('A patient cannot be the same as the doctor and vice versa.')


class Treatments(models.Model):
    appointment = models.ForeignKey(Appointment, related_name='treatments', on_delete=models.CASCADE)
    remarks = models.TextField(max_length=255)

    def __str__(self):
        return f"Treatment: {self.appointment} - Remarks: {self.remarks}"



class Announcement(models.Model):
    creator = models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return f"Announcement by {self.creator}: {self.description}"
    
    def clean(self):
        super().clean()  

        # check only super user or admin can make announcements
        if not self.creator.is_superuser:
            raise ValidationError('Only superusers can create announcements.')

    
