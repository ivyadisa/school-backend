from django.db import models


class Admission(models.Model):
    full_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


# ✅ Academics models
class Subject(models.Model):
    LEVEL_CHOICES = [
        ("primary", "Primary"),
        ("junior", "Junior Secondary"),
        ("senior", "Senior Secondary"),
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.level})"


class Department(models.Model):
    title = models.CharField(max_length=100)
    blurb = models.TextField()

    def __str__(self):
        return self.title


class DepartmentItem(models.Model):
    department = models.ForeignKey(Department, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.department.title}"


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Resource(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="resources/")  # upload PDFs etc.

    def __str__(self):
        return self.title


class Stat(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)  # e.g. "25+", "95%"

    def __str__(self):
        return f"{self.label}: {self.value}"
