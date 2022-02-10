from rest_framework import serializers


class NPVSerializer(serializers.Serializer):
    year = serializers.IntegerField(max_value=2050, min_value=2020)
    rate = serializers.FloatField()
