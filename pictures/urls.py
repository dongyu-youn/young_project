from django.urls import path
from . import views

app_name = "picture"

urlpatterns = [
    path("search/", views.search, name="search"), 
    path('toggle_favorite/<int:picture_id>/', views.toggle_favorite, name='toggle_favorite'),
]   