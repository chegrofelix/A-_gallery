from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> A+ GALLERY HOME</h1>')

def about(request):
    return HttpResponse('<h1> A+ GALLERY ABOUT</h1>')