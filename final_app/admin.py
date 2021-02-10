from django.contrib import admin
from .models import MyGallery
# Register your models here.
@admin.register(MyGallery)
class MyGallaryAdmin(admin.ModelAdmin):
    list_display = ['id','pic','dated','desc','catagory']

