import sys
from django.db import models
from io import BytesIO
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image

class Hotel(models.Model): 
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='MetaClean/') #(upload_to='images/')
    
    def save(self):
        im = Image.open(self.hotel_Main_Img)

        output = BytesIO()
        data = list(im.getdata())
        image_without_exif = Image.new(im.mode, im.size)
        image_without_exif.putdata(data)

        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        self.hotel_Main_Img = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.hotel_Main_Img.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Hotel,self).save()