from rest_framework.routers import DefaultRouter

from points.views import PointViewSet

router = DefaultRouter()

router.register(r'points', PointViewSet)