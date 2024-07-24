from hangar.views import (
    FeatureViewSet,
    AstronautViewSet,
    HangarViewSet,
    RacketViewSet,
    RacketFlightViewSet,
    OrderViewSet
)

from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register("features", FeatureViewSet)
router.register("astronauts", AstronautViewSet)
router.register("hangars", HangarViewSet),
router.register("rackets", RacketViewSet)
router.register("racket_flights", RacketFlightViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cosmodrome"
