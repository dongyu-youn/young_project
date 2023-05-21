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




    return render(request, "partials/pic_list.html", context={ "potato": pictures, "mind": mind_s, "color": color_s, "other": other_s, "shape": shapes_s})








def search(request):
    city = request.GET.get("city")

    

    shapes_s = models.Shape.objects.all()
    minds_s = models.Mind.objects.all()

    colors_s = models.Color.objects.all()
    others_s = models.Other.objects.all()

    shapes = request.GET.getlist("shape")
    colors = request.GET.getlist("color")
    minds = request.GET.getlist("mind")
    others = request.GET.getlist("other")

    print(shapes, colors, minds, others)
# request 요청
    filter_args = {}
# args안에 대입
   


    if len(shapes) > 0:
        for s_amenity in shapes:
            filter_args["shape__pk"] = int(s_amenity)
         
# 만약 shapes의 조건이

    if len(colors) > 0:
        for s in colors:
            filter_args["color__id"] = int(s)

    if len(minds) > 0:
        for abc in minds:
            filter_args["mind__id"] = int(abc)
    
    if len(others) > 0:
        for oo in others:
            filter_args["other__id"] = int(oo)

    
    if 'city' in request.GET: 
        filter_args["제목__contains"] = city
    picture = models.Picture.objects.all().filter(**filter_args)

 
   
    # query = None
    # if 'city' in request.GET: 
    #     query = request.GET.get('city') 
    #     products = models.Picture.objects.all().filter(Q(제목__contains=query))


    # filter_args = {}
    # if len(shapes_s) > 0:
    #     for s_amenity in shapes_s:
    #         filter_args["amenities__pk"] = int(s_amenity)

    # pictures = models.Picture.objects.filter(**filter_args)
    

    return render(request, "partials/search.html", {"abc": picture })

   
    
    