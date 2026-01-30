from django import forms
from django.contrib import admin

from .models import Games_Data, Genres, Platforms

# Register your models here.


class VideojuegoAdminForm(forms.ModelForm):
    class Meta:
        model = Games_Data
        fields = [
            "title",
            "description",
            "release_date",
            "genre",
            "platforms",
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
