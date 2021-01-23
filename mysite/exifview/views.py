from exifview.models import Hotel
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files import File
import os
import time
      
from exifview.forms import *

def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
        
        if form.is_valid():
            form.save()
            return redirect('exifview:success') 
    else: 
        form = HotelForm() 
    return render(request, 'exifview/hotel_image_form.html', {'form' : form}) 
  
  
def success(request):
    Hotels = Hotel.objects.all().last()
    delhotel = Hotel.objects.all().last().delete()
    remove_oldphotos()
    return render(request,'exifview/success.html',{'hotel_images' : Hotels})

# def display_hotel_images(request): 
  
#     if request.method == 'GET': 
  
#         # getting all the objects of hotel. 
#         Hotels = Hotel.objects.all()
#         return render (request, 'exifview/display_hotel_images.html', {'hotel_images' : Hotels})

def remove_all():
    """
    Delete all Tables in Row
    """
    Hotel.objects.all().delete()

def remove_oldphotos():
    """
    Removes photos older than 12 Hours.
    """
    path = os.getcwd()
    media_path = os.path.join(path,'media\\MetaClean')
    now = time.time()
    for filename in os.listdir(media_path):
        filestamp = os.stat(os.path.join(media_path, filename)).st_mtime
        filecompare = now - 0.5 * 86400 # Compares for every 12 hours
        if  filestamp < filecompare:
            os.remove(os.path.join(media_path, filename))