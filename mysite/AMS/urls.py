from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index_page,name='index'),
    path('edit_profile',views.edit_profile_page,name='edit_profile'),
    path('book_appointment',views.book_appointment_page,name='book_appointment'),
    path('prev_treatments',views.prev_treatments_page,name='prev_treatments'),
    path('login',views.login_page,name='login'),
    path('signup',views.signup_page,name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
