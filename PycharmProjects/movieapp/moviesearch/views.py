from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie  # Veendu, et see rida oleks olemas
import sqlite3

# Otsingufunktsioon
def search_movies(request):
    query = request.GET.get('query', '')
    print(f"Search query: {query}")  # Ajutine logimine
    movies = Movie.objects.filter(title__icontains=query)  # Veendu, et Movie on õigesti imporditud
    print(f"Movies found: {list(movies)}")  # Ajutine logimine
    context = {'movies': movies, 'query': query}
    return render(request, 'index.html', context)

# Kodulehe funktsioon
def home(request):
    return render(request, 'index.html')

# JSON andmete vaade
def movies_json(request):
    # Ühenda andmebaasiga
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Päring andmebaasi, et saada kõik filmide andmed
    cursor.execute('SELECT title, release_date, overview, poster_path FROM moviesearch_movie')
    movies = cursor.fetchall()

    # Sulge ühendus
    conn.close()

    # Loome JSON formaadis andmed
    movies_list = []
    for movie in movies:
        title, release_date, overview, poster_path = movie
        year = release_date[:4]  # Aasta vabastamise kuupäevast
        poster_image = f"https://image.tmdb.org/t/p/original{poster_path}" if poster_path else None

        movies_list.append({
            "title": title,
            "release_date": release_date,
            "year": year,
            "overview": overview,
            "poster_image": poster_image
        })

    # Tagastame JSON andmed
    return JsonResponse({"results": movies_list}, json_dumps_params={'indent': 2})

# URL-ide määramine
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_movies, name='search_movies'),
    path('movies-json/', views.movies_json, name='movies_json'),
]
