from hangar.serializers import (
    FeatureSerializer,
    AstronautSerializer,
    HangarSerializer,
    RacketSerializer,
    RacketListSerializer,
    RacketFlightSerializer,
    RacketFlightListSerializer,
    OrderSerializer,
    OrderCreateSerializer
)
from hangar.models import (
    Feature,
    Astronaut,
    Hangar,
    Racket,
    RacketFlight,
    Order,
)

from rest_framework.viewsets import ModelViewSet


class FeatureViewSet(ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class AstronautViewSet(ModelViewSet):
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer


class HangarViewSet(ModelViewSet):
    queryset = Hangar.objects.all()
    serializer_class = HangarSerializer


class RacketViewSet(ModelViewSet):
    queryset = Racket.objects.all()
    serializer_class = RacketSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = Racket.objects.all().prefetch_related("features", "astronauts")

        return queryset

    def get_serializer_class(self):
        serializer_class = self.serializer_class\

        if self.action == "list":
            serializer_class = RacketListSerializer

        return serializer_class


class RacketFlightViewSet(ModelViewSet):
    queryset = RacketFlight.objects.all()
    serializer_class = RacketFlightSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == "list":
            serializer_class = RacketFlightListSerializer

        return serializer_class


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == "create":
            serializer_class = OrderCreateSerializer

        return serializer_class
