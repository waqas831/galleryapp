from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=500)
    date_s=models.DateTimeField(auto_now_add=True)
    catagory=models.CharField(max_length=40)

    def __str__(self):
        return self.title+' '+self.catagory