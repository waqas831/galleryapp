from django.shortcuts import render
from django.http import HttpResponse
from .forms import GalleryForm
from .models import MyGallery

# Create your views here.

def index(request):
    if request.method=="POST":
        form=GalleryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=GalleryForm()
    img=MyGallery.objects.all()
    return render(request,'home.html',{'img':img,'form':form})

def search(request):
    if request.method=="GET":
        cat=request.GET.get('search')
        post=MyGallery.objects.all().filter(catagory=cat)
        return render(request,'search.html',{'post':post})




