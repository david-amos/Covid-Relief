from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    #return HttpResponse('<h1>hello</h1>')
    return render(request, 'loginApp/home.html')


def login(request):
    return HttpResponse('<h1>login</h1>')

def register(request):
    return HttpResponse('<h1>register</h1>')

