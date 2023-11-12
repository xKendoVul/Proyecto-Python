from django.db import models

# Create your models here.


class Genres(models.Model):
    genre = models.CharField(max_length=100)


class Games_Data(models.Model):
    port_image = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    date_sale = models.DateField("Fecha de salida")
    id_genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)


class Users(models.Model):
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_image = models.ImageField()


class Comment(models.Model):
    id_game = models.ForeignKey(Games_Data, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    Comment_text = models.CharField(max_length=500)
