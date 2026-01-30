from django.db import models

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
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    release_date = models.DateField()
    genre = models.ManyToManyField(Genres)
    platforms = models.ManyToManyField(Platforms)
    votes = models.IntegerField(blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
