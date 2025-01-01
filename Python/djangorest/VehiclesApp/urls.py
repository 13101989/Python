from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import tools, vehicles


router = DefaultRouter()
router.register(r"vehicles", vehicles.VehicleViewSet, "vehicle")
router.register(r"parts", vehicles.PartViewSet, "part")

urlpatterns = [
    path("tools", tools.get_tools),
    path("", include(router.urls)),
]
