from hangar.views import FeatureViewSet

from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register("features", FeatureViewSet)

urlpatterns = [
    path("", include(router.urls))
]


app_name = "cosmodrome"
