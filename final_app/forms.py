from django import forms
from .models import MyGallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model=MyGallery
        fields='__all__'
        labels={'pic':''}
    def __init__(self,*args,**kwargs):
        super(GalleryForm,self).__init__(*args,**kwargs)
        self.fields['desc'].widget.attrs['style']='width:300px;height:80px;color:white;'
