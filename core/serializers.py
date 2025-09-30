from rest_framework import serializers
from .models import Admission, Contact, Subject, Department, DepartmentItem, FAQ, Resource, Stat


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class DepartmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentItem
        fields = ["id", "name"]


class DepartmentSerializer(serializers.ModelSerializer):
    items = DepartmentItemSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ["id", "title", "blurb", "items"]


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = "__all__"
