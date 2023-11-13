from django import forms
from django.contrib import admin
from .models import Genres, Games_Data, Users, Comment, Platforms

# Register your models here.


class VideojuegoAdminForm(forms.ModelForm):
    class Meta:
        model = Games_Data
        fields = [
            "port_image",
            "title",
            "description",
            "date_sale",
            "genre",
            "platforms",
            "votes",
            "game_time",
        ]

    platforms = forms.ModelMultipleChoiceField(
        queryset=Platforms.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    genre = forms.ModelMultipleChoiceField(
        queryset=Genres.objects.all(), widget=forms.CheckboxSelectMultiple
    )


class VideojuegoAdmin(admin.ModelAdmin):
    form = VideojuegoAdminForm


admin.site.register(Games_Data, VideojuegoAdmin)
admin.site.register(Platforms)
admin.site.register(Genres)
admin.site.register(Users)
admin.site.register(Comment)
