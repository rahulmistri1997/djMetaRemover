from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files import File


from exifview.forms import *


def index(request):
    return HttpResponse("Hello, world")

def test(request):
    return render(request,'exifview/index.html')

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
    return render(request,'exifview/success.html',{'hotel_images' : Hotels})

def display_hotel_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Hotels = Hotel.objects.all()
        return render (request, 'exifview/display_hotel_images.html', {'hotel_images' : Hotels})