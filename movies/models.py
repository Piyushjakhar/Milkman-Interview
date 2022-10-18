from django.db import models

from movies.base import SoftDeletionModel


# Create your models here.

class Theaters(SoftDeletionModel):
    name = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    is_active = models.BooleanField(default=True)


class Movies(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    is_active = models.BooleanField(default=True)


class TheaterMovieMapping(SoftDeletionModel):
    theater = models.ForeignKey('Theaters', related_name="related_theater_mappings", on_delete=models.CASCADE)
    movie = models.ForeignKey('Movies', related_name="related_movie_mappings", on_delete=models.CASCADE)
    price = models.PositiveIntegerField(blank=False, null=False)

