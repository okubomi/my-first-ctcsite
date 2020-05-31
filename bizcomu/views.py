from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    トップ画面
    """
    return HttpResponse("bizcomu Hello, world.")

