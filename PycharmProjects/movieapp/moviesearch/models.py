from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    overview = models.TextField(blank=True, null=True)  # Veendu, et `overview` on olemas
    poster_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
