from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Это приложение catalog — всё работает!")

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')