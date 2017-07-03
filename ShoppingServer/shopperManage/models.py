# --*-- coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.template.loader import render_to_string

# Create your models here.

class Image(models.Model):  
    name = models.CharField(max_length=30)  
    image = models.ImageField(upload_to='images/')
          
    def __unicode__(self):  
        return self.name  
        
    def thumbnail(self):
        image_path = """<img src="%s" height="40">"""  % (self.image.url)
        return image_path
        #return render_to_string('thumb.html', {'image':self})
 
 
  
class ImageAdmin(admin.ModelAdmin):
    list_display=["__unicode__","name","thumbnail"]  #Åã¥ÜÄæ

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()      
  
admin.site.register(Image, ImageAdmin) 

class Product(models.Model):
    seller = models.CharField(max_length=60)
    sellerid = models.IntegerField(default=0)
    product_name = models.CharField(max_length=60)
    product_attr = models.CharField(max_length=30)
    product_price = models.IntegerField()
    product_img = models.TextField()
    product_buyer = models.CharField(max_length=60, default="")
    product_buyerid = models.IntegerField(default=0)
    product_uploadtime = models.IntegerField(default=0)
