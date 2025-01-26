from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('user/', include('user_manager.urls')),
    path('sp/', include('statuspage_manager.urls')),
    path('', admin.site.urls),
]
