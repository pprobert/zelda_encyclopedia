from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("zelda/", include("zelda.urls")),
    path("admin/", admin.site.urls),
]