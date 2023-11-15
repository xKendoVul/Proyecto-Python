from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from Videogames import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registro/", views.registro, name="registro"),
    path("", include("Videogames.urls")),
    path("bienvenida/", views.bienvenida, name="bienvenida"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
