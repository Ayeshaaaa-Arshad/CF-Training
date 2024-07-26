from .models import *
from django.db.models import Count, Q
from django.db.models.functions import *


class AppointmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-date')

    def with_patient_true_status_count(self):
        return self.get_queryset().filter(status=True).values('patient').annotate(
            count=Coalesce(Count('id'), 0)
        ).order_by('-count')

    def with_doctor_true_status_count(self):
        return self.get_queryset().filter(status=True).values('doctor').annotate(
            count=Coalesce(Count('id'), 0)
        ).order_by('-count')