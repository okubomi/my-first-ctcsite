from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path("", views.index, name='index'),
    path("user_create/", views.user_create, name='user_create'),
    path("user_create_complete/", views.user_create_complete, name="user_create_complete"),
    path("user_list/", views.user_list, name='user_list'),
    path("user_detail/<int:pk>/", views.user_detail, name='user_detail'),
    path("user_find/", views.user_find, name='user_find'),

]