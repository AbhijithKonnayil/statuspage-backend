
from django.db import models

from user_manager.models import Organization

STATUS_CHOICES = [
    ('Operational', 'Operational'),
    ('Degraded', 'Degraded Performance'),
    ('Partial Outage', 'Partial Outage'),
    ('Major Outage', 'Major Outage'),
]


class Service(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Operational')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name


class ServiceHistory(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, null=False)
    date = models.DateField()

    def __str__(self):
        return f"{self.service} f{self.date} - ${self.status}"


class Incident(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='incidents')
    title = models.CharField(max_length=255)
    description = models.TextField()
    STATUS_CHOICES = [
        ('Investigating', 'Investigating'),
        ('Monitoring', 'Monitoring'),
        ('Resolved', 'Resolved'),
    ]
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Investigating')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IncidentUpdate(models.Model):
    incident = models.ForeignKey(
        Incident, on_delete=models.CASCADE, related_name='updates')
    update_text = models.TextField()
    status = models.CharField(max_length=50, choices=Incident.STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.incident.title}"


class Maintenance(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='maintenances')
    title = models.CharField(max_length=255)
    description = models.TextField()
    scheduled_start = models.DateTimeField()
    scheduled_end = models.DateTimeField()
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
