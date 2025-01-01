from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"titles", views.TitlesViewSet, "title")
router.register(r"mass_delete", views.MassDeleteArtifactsViewSet, "mass-delete")

urlpatterns = [
    path("v1/listing/", views.listing),
    path("v1/", include(router.urls)),
]

# curl -X DELETE -d "ids=1,2,4,5,6" http://127.0.0.1:80/api/v1/mass_delete/mass_delete/