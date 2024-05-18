from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

from authentication.models import MyUser


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    directors = models.ForeignKey(Director, on_delete=models.CASCADE)
    imdb_rating = models.FloatField()
    imdb_votes = models.IntegerField(default=0)
    imdb_votes_average = models.FloatField(default=0)
    imdb_ratings_average = models.FloatField(default=0)
    imdb_ratings_count = models.IntegerField(default=0)
    imdb_votes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Saved(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user


class Transaction(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
