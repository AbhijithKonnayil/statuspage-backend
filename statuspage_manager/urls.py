
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (IncidentUpdateViewSet, IncidentViewSet, MaintenanceViewSet,
                    ServiceViewSet)


router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'incidents', IncidentViewSet)
router.register(r'incident-updates', IncidentUpdateViewSet)
router.register(r'maintenances', MaintenanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
