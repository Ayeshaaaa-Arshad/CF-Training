from django.db import models

class User(models.Model):
    GENDER_TYPE = [
        ("F", "Female"),
        ("M", "Male"),
        ("N", "Rather not say")
    ]

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=50,blank=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)  
    gender = models.CharField(max_length=1, choices=GENDER_TYPE)
    image = models.ImageField(upload_to='profile_images/', verbose_name='Profile Image', blank=True, null=True)

    class Meta:
        abstract = True

class Patient(User):
    age = models.PositiveIntegerField()
    email = None

    def __str__(self):
        return f"Patient: {self.first_name} {self.last_name}, Age: {self.age}"

class Doctor(User):
    designation = models.CharField(max_length=255)

    def __str__(self):
        return f"Doctor: {self.first_name} {self.last_name}, Designation: {self.designation}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f"Appointment: {self.patient} with {self.doctor} on {self.date}"

class Treatment(models.Model):
    appointment = models.ForeignKey(Appointment, related_name='treatments', on_delete=models.CASCADE)
    remarks = models.TextField(max_length=255)

    def __str__(self):
        return f"Treatment: {self.appointment} - Remarks: {self.remarks}"

class Announcement(models.Model):
    creator = models.ForeignKey(Doctor, related_name='announcements', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Announcement by {self.creator}: {self.description}"
