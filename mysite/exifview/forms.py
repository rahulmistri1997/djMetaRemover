from django import forms 
from exifview.models import *
  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Hotel 
        fields = ['name', 'hotel_Main_Img'] 