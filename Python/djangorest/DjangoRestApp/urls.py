from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include("PeopleApp.urls")),
    path("api/", include("ArtifactsApp.urls")),
    path("api/", include("BooksApp.urls")),
    path("api/", include("VehiclesApp.urls")),
    path("api/", include("SinglePageApp.urls")),
]
