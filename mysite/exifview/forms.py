from django import forms
from django.forms import widgets 
from exifview.models import *
  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Hotel 
        fields = ['hotel_Main_Img'] 

        widget = {
            'hotel_Main_Img' : forms.FileInput(attrs={'class' : 'form-control'})
        }