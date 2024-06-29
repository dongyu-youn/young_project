from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import BooleanField, Case, When
from django.db.models import Count

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

   
    search_history = models.SearchHistory.objects.exclude(count=0).order_by('-count')[:8]
 
    return render(request, "partials/pic_list.html", context={ "potato": pictures, "mind": mind_s, "color": color_s, "other": other_s, "shape": shapes_s, "history": search_history})




def search(request):
    city = request.GET.get("city")

    shapes_s = models.Shape.objects.all()
    mind_s = models.Mind.objects.all()
    color_s = models.Color.objects.all()
    other_s = models.Other.objects.all()

    shapes = request.GET.getlist("shape")
    colors = request.GET.getlist("color")
    minds = request.GET.getlist("mind")
    others = request.GET.getlist("other")

    filter_args = {}

    if len(shapes) > 0:
        for s_amenity in shapes:
            filter_args["shape__id"] = int(s_amenity)
         
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

    search_history = None
    if city:
        search_history = models.SearchHistory(query=city, user = request.user)
        search_history.save()

    if city and request.user.is_authenticated:
        search_history_list = models.SearchHistory.objects.filter(query=city, user=request.user)
        if search_history_list.exists():  # 조건에 맞는 객체가 존재하는지 확인
            search_history = search_history_list.first()  # 첫 번째 객체 선택
            search_history.count += 1
            search_history.save()
        else:
            # 새로운 검색어라면 객체를 생성하여 저장
            search_history = models.SearchHistory(query=city, user=request.user, count=1)
            search_history.save()

    

    search_history_list = models.SearchHistory.objects.order_by('-timestamp')[:8]

    query = request.GET.get("query")

    print(picture)
    return render(request, "partials/search.html", {"abc": picture, "mind": mind_s, "color": color_s, "other": other_s, "shape": shapes_s, "city": city, 'search': search_history_list, 'query': query})

   
@login_required
def toggle_favorite(request, picture_id):
    picture = models.Picture.objects.get(pk=picture_id)
    user = request.user

    try:
        favorite = models.Favorite.objects.get(user=user, picture=picture)
        favorite.delete()
        liked = False
    except models.Favorite.DoesNotExist:
        favorite = models.Favorite(user=user, picture=picture)
        favorite.save()
        liked = True

    data = {
        'liked': liked,
        'count': picture.favorite_set.count()
    }
    return JsonResponse(data)