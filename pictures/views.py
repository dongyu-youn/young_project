from django.shortcuts import render
from . import models
# Create your views here.


def home_pictures(request):
    all_pictures = models.Picture.objects.all()
 

    return render(request, "home.html", context={"sweet": all_pictures})


def all_pictures(request):
    
    all_pictures = models.Picture.objects.all()
    

    


    return render(request, "partials/pic_list.html", context={"potato": all_pictures})