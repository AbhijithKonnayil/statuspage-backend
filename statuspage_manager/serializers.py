from collections import defaultdict
from datetime import date, timedelta

from rest_framework import serializers

from .models import (Incident, IncidentUpdate, Maintenance, Service,
                     ServiceHistory)


class ServiceSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()
    uptime = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = '__all__'

    def update(self, instance, validated_data):
        ServiceHistory.objects.create(
            service=instance, status=instance.status, date=date.today())
        instance = super().update(instance, validated_data)
        return instance

    def get_history(self, obj):
        # Get the last 10 entries from the ServiceHistory model related to this service
        history_entries = (
            ServiceHistory.objects.filter(service=obj)
            .order_by('-date')[:10]
            .values('date', 'status')
        )

        # Organize the statuses by date
        history_dict = defaultdict(list)
        for entry in history_entries:
            date_str = entry['date'].strftime('%d-%m-%Y')
            history_dict[date_str].append(entry['status'])

        # Ensure the history is in descending order of date
        return dict(sorted(history_dict.items(), reverse=True))

    def get_uptime(self, obj):
        # Calculate uptime for the last 50 days
        today = date.today()
        start_date = today - timedelta(days=50)

        # Get ServiceHistory entries for the last 50 days
        history_entries = ServiceHistory.objects.filter(
            service=obj,
            date__gte=start_date,
            date__lte=today
        ).values('date', 'status')

        # Initialize a dictionary to store the status for each day
        status_dict = {start_date +
                       timedelta(days=i): 'Operational' for i in range(50)}

        # Fill the dictionary with the status data from ServiceHistory
        for entry in history_entries:
            status_dict[entry['date']] = entry['status']

        # Calculate the number of days the service was operational
        uptime_days = sum(1 for status in status_dict.values()
                          if status == 'Operational')

        # Calculate uptime percentage
        uptime_percentage = (uptime_days / 50) * 100

        return {
            'uptime_days': uptime_days,
            'uptime_percentage': uptime_percentage
        }


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'


class IncidentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentUpdate
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'
