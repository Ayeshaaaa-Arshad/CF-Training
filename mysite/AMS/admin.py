from django.contrib import admin
from .models import *


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Announcement)
admin.site.register(Appointment)
admin.site.register(Treatment)