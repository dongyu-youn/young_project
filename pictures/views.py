from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def home_pictures(request):
    all_pictures = models.Picture.objects.all()[:4]
    return render(request, "home.html", context={"sweet": all_pictures})


def all_pictures(request):
    page = request.GET.get("page")
    all_picture = models.Picture.objects.all()
    paginator = Paginator(all_picture, 8)
    pictures = paginator.get_page(page)

    shapes_s = models.Shape.objects.all()
    mind_s = models.Mind.objects.all()
    color_s = models.Color.objects.all()
    other_s = models.Other.objects.all()
    

    return render(request, "partials/pic_list.html", context={"abc": pictures, "abcd": shapes_s, "mind": mind_s, "color": color_s, "other": other_s})








def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city) # 👈 앞 단어 대문자로 처리 
    minds = request.GET.get("mind")
    shapes = request.GET.get("shape")
    colors = request.GET.get("color")
    others = request.GET.get("other")

    shapes_s = models.Shape.objects.all()
    minds_s = models.Mind.objects.all()

    colors_s = models.Color.objects.all()
    others_s = models.Other.objects.all()


   

  
    
    query = None
    if 'city' in request.GET: 
        query = request.GET.get('city') 
        products = models.Picture.objects.all().filter(Q(제목__contains=query))
    return render(request, "partials/search.html", {"query": query, "products": products})

   
    
    