"""
URL configuration for config project.
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("home/", include("core_apps.home.urls")),
]


admin.site.site_header = "Roots Apartment Admin"
admin.site.site_title = "Roots Apartment Admin Portal"
admin.site.index_title = "Welcome to Roots Apartment Admin Portal"
