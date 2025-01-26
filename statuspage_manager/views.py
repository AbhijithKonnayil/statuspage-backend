from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Incident, IncidentUpdate, Maintenance, Service
from .serializers import (IncidentSerializer, IncidentUpdateSerializer,
                          MaintenanceSerializer, ServiceSerializer)


class OrgQuerysetMixin:
    def get_queryset(self):
        org = self.request.query_params.get("org", None)
        params = {}
        if (org):
            params.update({"organization__name": org})
        return super().get_queryset().filter(**params)


class ServiceViewSet(OrgQuerysetMixin, viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class IncidentUpdateViewSet(viewsets.ModelViewSet):
    queryset = IncidentUpdate.objects.all()
    serializer_class = IncidentUpdateSerializer


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
