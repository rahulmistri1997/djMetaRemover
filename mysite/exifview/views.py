from django.http import HttpResponse
from django.shortcuts import render, redirect

from io import BytesIO
from django.core.files import File
from PIL import Image

from exifview.forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    return render(request,'exifview/index.html')

def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
        
        if form.is_valid():
            form.save()
            return redirect('exifview:success()') 
    else: 
        form = HotelForm() 
    return render(request, 'exifview/hotel_image_form.html', {'form' : form}) 
  
  
def success(request):
    return render(request,'exifview/success.html')

def display_hotel_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Hotels = Hotel.objects.all()  
        return render (request, 'exifview/display_hotel_images.html', {'hotel_images' : Hotels})

def download_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Hotels = Hotel.objects.all()
        return render (request, 'exifview/display_hotel_images.html', {'hotel_images' : Hotels})