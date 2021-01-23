from django.urls import path
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 
from exifview.views import *
from . import views

app_name = 'exifview'

urlpatterns = [
    path('', views.hotel_image_view, name='image_upload'),
    path('success/', views.success, name = 'success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)