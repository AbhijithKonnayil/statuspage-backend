from django.contrib import admin

from .models import *

admin.site.register(Service)
admin.site.register(Incident)
admin.site.register(IncidentUpdate)
admin.site.register(Maintenance)
admin.site.register(ServiceHistory)
