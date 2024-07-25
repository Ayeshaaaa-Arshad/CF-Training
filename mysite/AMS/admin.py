from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
    verbose_name = "Patient"
    verbose_name_plural = "Patients"

class DoctorAdmin(admin.ModelAdmin):
    verbose_name = "Doctor"
    verbose_name_plural = "Doctors"

admin.site.register(Patient,PatientAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Announcement)
admin.site.register(Appointment)
admin.site.register(Treatments)
admin.site.register(CustomUser)