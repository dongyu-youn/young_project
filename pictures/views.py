from django.shortcuts import render

# Create your views here.


def home_pictures(request):
    
    return render(request, "home.html")