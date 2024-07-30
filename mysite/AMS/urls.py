from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.IndexPageView.as_view(),name='index'),
    path('edit_profile',views.EditProfileView.as_view(),name='edit_profile'),
    path('book_appointment/<int:pk>',views.BookAppointmentView.as_view(),name='book_appointment'),
    path('treatments',views.TreatmentView.as_view(),name='treatments'),
    path('login',views.login_page,name='login'),
    path('signup',views.signup_page,name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
