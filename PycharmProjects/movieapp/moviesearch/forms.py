# moviesearch/forms.py
from django import forms

class MovieSearchForm(forms.Form):
    query = forms.CharField(label='Movie Title', max_length=100)
