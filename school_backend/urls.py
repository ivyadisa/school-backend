# school_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Root redirect view
def redirect_root(request):
    return redirect("/api/hello/")

urlpatterns = [
    path("", redirect_root),          # Redirect root URL to /api/hello/
    path("admin/", admin.site.urls),  # Admin panel
    path("api/", include("core.urls")),  # Include your API endpoints
]
