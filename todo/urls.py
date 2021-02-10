from django.urls import path
from todo import views

urlpatterns = [
    path('',views.index,name="todo_index"),
    path('update/<int:id>',views.update,name="update"),
    ]