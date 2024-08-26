from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Esilehe URL
    path('search/', views.search_movies, name='search_movies'),  # Otsingu URL
    path('movies-json/', views.movies_json, name='movies_json'),  # JSON andmete URL
]
