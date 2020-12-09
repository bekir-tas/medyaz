from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class News(models.Model):
    image = models.FileField()
    baslik = models.CharField(max_length=250)
    tanitim = models.TextField()
    icerik = RichTextField('upload_to=medyaz')
    tarih = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
"""
class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    icerik = models.TextField(max_length=3000)
    tarih = models.DateTimeField(auto_now_add=True)
"""    
