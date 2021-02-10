from django import forms
from django.forms import ModelForm
from todo.models import Todo

class TodoModel(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'


    def __init__(self,*args,**kwargs):
        super(TodoModel, self).__init__(*args,**kwargs)
        self.fields['desc'].widget.attrs['style']='background:red;padding:12px;white-space:pre;'
        self.fields['catagory'].widget.attrs['style'] = 'background:red;padding:12px;'
        self.fields['desc'].widget.attrs['style'] = 'background:red;padding:12px;'
        self.fields['title'].widget.attrs['style'] = 'background:red;padding:12px;'