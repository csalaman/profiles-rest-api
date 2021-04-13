# Define the API path for profile_api app/service (aka the app_name/urls.py)
from django.contrib import admin
from profile_api import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profile_api.urls')),
]
