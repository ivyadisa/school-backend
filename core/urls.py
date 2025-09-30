from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_api),
    path("admission/", views.admission_api),
    path("contact/", views.contact_api),

    # ✅ Academics
    path("subjects/", views.subjects_api),
    path("subjects/<str:level>/", views.subjects_api),  # /api/subjects/junior/
    path("departments/", views.departments_api),
    path("faqs/", views.faqs_api),
    path("resources/", views.resources_api),
    path("stats/", views.stats_api),
]
