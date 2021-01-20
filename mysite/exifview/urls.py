from django.urls import path
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 
from exifview.views import *
from . import views

app_name = 'exifview'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('image_upload/', views.hotel_image_view, name = 'image_upload'), 
    path('success/', views.success, name = 'success'),
    path('hotel_images/', views.display_hotel_images, name = 'hotel_images'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)