from django.db import models

# Create your models here.
class MyGallery(models.Model):
    pic=models.ImageField(upload_to="image",default="")
    dated=models.DateTimeField(auto_now_add=True)
    desc=models.TextField(default="")
    catagory=models.CharField(max_length=50,default="")