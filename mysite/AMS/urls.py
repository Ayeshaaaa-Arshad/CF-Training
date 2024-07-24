from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index_page,name='index'),
    path('edit_profile',views.edit_profile_page,name='edit_profile'),
    path('book_appointment',views.book_appointment_page,name='book_appointment'),
    path('prev_treatment',views.prev_treatment_page,name='prev_treatment'),
    path('login_signup',views.login_singup_page,name='login_signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
