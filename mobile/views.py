from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(about):
    return render(request, 'about.html')