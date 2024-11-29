from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('api/', include('verification.urls')),  # API endpoints
    path('admin/', admin.site.urls),  # Admin panel
]
