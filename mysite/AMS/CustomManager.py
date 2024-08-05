from .models import *
from django.db.models import Count, Q
from django.db.models.functions import *
from django.contrib.auth.models import BaseUserManager

# Custom Manager Now Appointment will have by default manager's dunctionalities plus these below
class AppointmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-appointment_date')

    #All patient with their respected count
    def patients_appointments_counts(self):
        return self.get_queryset().filter(status=True).values('patient').annotate(
            count=Coalesce(Count('id'), 0)
        ).order_by('-count')

    #All Doctors with their respected count
    def doctors_appointments_counts(self):
        return self.get_queryset().filter(status=True).values('doctor').annotate(
            count=Coalesce(Count('id'), 0)
        ).order_by('-count')
    
class UserManager(BaseUserManager):
    """
     Create and return a user with an email and password.
    """
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('Email Field is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
