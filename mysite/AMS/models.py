from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_image_file_extension
from django.core.exceptions import ValidationError
    

    
class CustomUser(AbstractUser):
    GENDER_TYPE = [
        ("F","Female"),
        ("M","Male"),
        ("O","Other")
    ]

    gender = models.CharField(max_length=1, choices=GENDER_TYPE)
    image = models.ImageField(upload_to='profile/images',verbose_name='Profile Image',blank=True,null=True,validators=[validate_image_file_extension])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Patient(CustomUser):
    age = models.PositiveIntegerField()
    email = None

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"Patient: {self.first_name} {self.last_name}, Age: {self.age}"

class Doctor(CustomUser):
    designation = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctor"

    def __str__(self):
        return f"Doctor: {self.first_name} {self.last_name}, Designation: {self.designation}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f"Appointment: {self.patient} with {self.doctor} on {self.date}"

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
        if not self.creator.is_superuser:
            raise ValidationError('Only superusers can create announcements.')

    
