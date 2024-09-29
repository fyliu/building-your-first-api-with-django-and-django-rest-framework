from django.urls import path, include
from rest_framework import routers

from .views import ArtistViewSet

router = routers.DefaultRouter()
router.register(r"artists", ArtistViewSet)

urlpatterns = [
    path("", include(router.urls)),
]