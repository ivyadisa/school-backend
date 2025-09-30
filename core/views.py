from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.mail import send_mail
from .models import Admission, Contact, Subject, Department, FAQ, Resource, Stat
from .serializers import (
    AdmissionSerializer,
    ContactSerializer,
    SubjectSerializer,
    DepartmentSerializer,
    FAQSerializer,
    ResourceSerializer,
    StatSerializer,
)


@api_view(["GET"])
def hello_api(request):
    return Response({"message": "Hello from Django Backend!"})


@api_view(["POST"])
def admission_api(request):
    serializer = AdmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def contact_api(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        contact = serializer.save()  # Save to DB

        # Send email
        subject = f"New Contact Message from {contact.name}"
        message = f"""
You have a new message from {contact.name} ({contact.email}).

Message:
{contact.message}
"""
        send_mail(
            subject,
            message,
            "no-reply@schoolname.ac.ke",   # From (set a default sender)
            ["ivymakokha07@gmail.com"],     # To (admin email)
            fail_silently=False,
        )

        return Response(
            {"success": True, "data": serializer.data, "message": "Email sent successfully!"},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Academics APIs
@api_view(["GET"])
def subjects_api(request, level=None):
    if level:
        subjects = Subject.objects.filter(level=level)
    else:
        subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def departments_api(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def faqs_api(request):
    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def resources_api(request):
    resources = Resource.objects.all()
    serializer = ResourceSerializer(resources, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def stats_api(request):
    stats = Stat.objects.all()
    serializer = StatSerializer(stats, many=True)
    return Response(serializer.data)
