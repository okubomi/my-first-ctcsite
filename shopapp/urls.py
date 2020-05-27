from django.conf.urls import url
from . import views

urlpatterns = [
    url('index/', views.index, name='index'),
    url(r'^form/', views.form, name='form'),
    url(r'^addcartform/', views.addcartform, name='addcartform'),
    url(r'^lookcart/', views.lookcart, name='lookcart'),
    url(r'^changeorderquantity/', views.changeorderquantity, name='changeorderquantity'),  
    url(r'^deletecartrecord/', views.deletecartrecord, name='deletecartrecord'),

]