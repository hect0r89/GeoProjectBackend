from rest_framework import serializers

from points.models import Point


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('lat', 'lon', 'radius', 'message', 'id', 'device_id')
