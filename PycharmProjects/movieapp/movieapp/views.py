# movieapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import MovieSearchForm

TMDB_API_KEY = 'your_tmdb_api_key_here'  # Replace with your actual TMDB API Key

def search(request):
    form = MovieSearchForm()
    movies = []

    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            response = requests.get(
                f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}'
            )
            if response.status_code == 200:
                data = response.json()
                movies = data.get('results', [])

    return render(request, 'movieapp/search.html', {'form': form, 'movies': movies})
