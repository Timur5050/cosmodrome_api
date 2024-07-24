from rest_framework import serializers

from hangar.models import (
    Feature,
    Astronaut,
    Hangar,
    Racket,
    RacketFlight,
    Order, Ticket,
)


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ("id", "name")


class AstronautSerializer(serializers.ModelSerializer):
    class Meta:
        model = Astronaut
        fields = ("id", "first_name", "last_name", "full_name")


class HangarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hangar
        fields = ("id", "name", "rackets_number")


class RacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racket
        fields = ("id", "name", "type", "height", "features", "astronauts")


class RacketListSerializer(RacketSerializer):
    features = serializers.StringRelatedField(many=True)
    astronauts = serializers.StringRelatedField(many=True)


class RacketFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = RacketFlight
        fields = ("id", "flight_time", "racket", "hangar")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "racket_flight", "racket_number")


class RacketFlightListSerializer(serializers.ModelSerializer):
    racket_name = serializers.CharField(source="racket.name")
    racket_height = serializers.CharField(source="racket.height")
    hangar_name = serializers.CharField(source="hangar.name")
    taken_tickets = TicketSerializer(many=True, source="tickets")

    class Meta:
        model = RacketFlight
        fields = ("id", "flight_time", "racket_name", "racket_height", "hangar_name", "taken_tickets")


class TicketOrderSerializer(TicketSerializer):
    racket_flight = RacketFlightListSerializer()


class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "created_at", "tickets")


class OrderCreateSerializer(OrderSerializer):
    tickets = TicketSerializer(many=True)

    def create(self, validated_data):
        tickets = validated_data.pop("tickets")
        order = Order.objects.create(**validated_data)
        for ticket in tickets:
            Ticket.objects.create(**ticket, order=order)

        return order
