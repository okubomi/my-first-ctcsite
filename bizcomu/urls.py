from django.urls import path
from . import views

app_name='bizcomu'

urlpatterns = [
    path("", views.index, name='index'),
 
]