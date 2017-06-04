from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, ListModelMixin, CreateModelMixin, \
    DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from points.models import Point
from points.serializers import PointSerializer


class PointViewSet(GenericViewSet,UpdateModelMixin,RetrieveModelMixin, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
