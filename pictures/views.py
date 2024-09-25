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

    # 여기서 search history를 불러오고 템플릿에 전달
    search_history = models.SearchHistory.objects.exclude(count=0).order_by('-count')[:8]
 
    return render(request, "partials/pic_list.html", context={ 
        "potato": pictures, 
        "mind": mind_s, 
        "color": color_s, 
        "other": other_s, 
        "shape": shapes_s, 
        "history": search_history  # history를 템플릿에 전달
    })




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

    # Picture 모델에 있는 필드로 필터링 진행
    if len(shapes) > 0:
        for shape in shapes:
            filter_args["shape__id"] = int(shape)  # department 대신 shape로 수정
         
    if len(colors) > 0:
        for color in colors:
            filter_args["color__id"] = int(color)  # species 대신 color로 수정

    if len(minds) > 0:
        for mind in minds:
            filter_args["mind__id"] = int(mind)  # mind 필드 그대로 사용
    
    if len(others) > 0:
        for other in others:
            filter_args["other__id"] = int(other)  # other 필드 그대로 사용

    if city:
        filter_args["제목__contains"] = city  # 제목 필드가 맞는지 확인 필요

    # 필터링된 결과 가져오기
    picture = models.Picture.objects.all().filter(**filter_args)

    # 검색 기록 저장 로직
    if city and request.user.is_authenticated:
        search_history_list = models.SearchHistory.objects.filter(query=city, user=request.user)
        if search_history_list.exists():
            search_history = search_history_list.first()
            search_history.count += 1
            search_history.save()
        else:
            search_history = models.SearchHistory(query=city, user=request.user, count=1)
            search_history.save()

    # 최근 검색 기록 가져오기
    search_history_list = models.SearchHistory.objects.order_by('-timestamp')[:8]

    query = request.GET.get("query")

    return render(request, "partials/search.html", {
        "abc": picture,
        "mind": mind_s,
        "color": color_s,
        "other": other_s,
        "shape": shapes_s,
        "city": city,
        "search": search_history_list,
        "query": query
    })

   
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