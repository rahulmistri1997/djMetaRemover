from django import forms
from django.forms import widgets 
from exifview.models import *

class HotelForm(forms.ModelForm): # Images Upload Form TODO: Name Change
  
    class Meta: 
        model = Hotel 
        fields = ['Image_To_Clean'] 

        widget = {
            'Image_To_Clean' : forms.FileInput(attrs={'class' : 'form-control'})
        }