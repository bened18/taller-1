from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page from Benjamin</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name':'Benjamin Eduardo De La Torre Rojas'})

def about(request):
    return render(request, 'about.html', {'name':'Benjamin De La Torre'})