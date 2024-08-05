from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.IndexPageView.as_view(),name='index'),
    path('login',views.LoginView.as_view(),name='login'),
    path('signup',views.SignupView.as_view(),name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('doctors/', views.DoctorListView.as_view(), name='doctor_list'),
    path('receptionists/', views.ReceptionistListView.as_view(), name='receptionist_list'),
    path('appointments/',views.AppointmentView.as_view(),name='appointment_list'),
    path('treatments',views.TreatmentView.as_view(),name='treatment_list'),
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    path('patient/create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('patient/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient_update'),
    path('patient/<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient_delete'),
    path('doctors/create/', views.DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/<int:pk>/edit/', views.DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/<int:pk>/delete/', views.DoctorDeleteView.as_view(), name='doctor_delete'),
    path('receptionist/create/', views.ReceptionistCreateView.as_view(), name='receptionist_create'),
    path('receptionist/<int:pk>/edit/', views.ReceptionistUpdateView.as_view(), name='receptionist_update'),
    path('receptionist/<int:pk>/delete/', views.ReceptionistDeleteView.as_view(), name='receptionist_delete'),
    path('book_appointment',views.BookAppointmentView.as_view(),name='book_appointment'),
    path('update_appointment/<int:pk>/', views.UpdateAppointmentView.as_view(), name='update_appointment'),
    path('cancel_appointment/<int:pk>/', views.CancelAppointmentView.as_view(), name='cancel_appointment'),
    path('announcements/', views.AnnouncementListView.as_view(), name='announcement_list'),
    path('announcements/<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement_list'),
    path('announcements/create/', views.AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcements/<int:pk>/update/', views.AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('announcements/<int:pk>/delete/', views.AnnouncementDeleteView.as_view(), name='announcement_delete'),
    path('treatments/create/', views.TreatmentCreateView.as_view(), name='treatment_create'),
    path('treatments/<int:pk>/update/', views.TreatmentUpdateView.as_view(), name='treatment_update'),
    path('treatment/create/', views.TreatmentCreateView.as_view(), name='treatment_create'),
    path('treatment/<int:pk>/update/', views.TreatmentUpdateView.as_view(), name='treatment_update'),
    path('diseases/', views.DiseaseListView.as_view(), name='disease_list'),
    path('diseases/create/', views.DiseaseCreateView.as_view(), name='disease_create'),
    path('diseases/update/<int:pk>/', views.DiseaseUpdateView.as_view(), name='disease_update'),
    path('diseases/delete/<int:pk>/', views.DiseaseDeleteView.as_view(), name='disease_delete'),
    path('edit_profile <int:pk>',views.EditProfileView.as_view(),name='edit_profile'),
    path('provide_feedback/<int:treatment_id>/',views.FeedbackFormView.as_view(), name='provide_feedback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

