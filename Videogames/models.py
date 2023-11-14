from django.db import models
from django import forms

# Create your models here.


class Genres(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Platforms(models.Model):
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.platform


class Games_Data(models.Model):
    port_image = models.ImageField(upload_to="Videogames/images/games")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    date_sale = models.DateField()
    genre = models.ManyToManyField(Genres)
    platforms = models.ManyToManyField(Platforms)
    votes = models.IntegerField(default=0)
    game_time = models.CharField(max_length=8)

    def __str__(self):
        return self.title


class Users(models.Model):
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_image = models.ImageField(upload_to="Videogames/images/users")


class Comment(models.Model):
    id_game = models.ForeignKey(Games_Data, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    Comment_text = models.CharField(max_length=500)
    date_published = models.DateTimeField()
