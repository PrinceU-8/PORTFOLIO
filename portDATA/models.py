from django.db import models

class ProjDATA(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=367)
    link = models.URLField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.project_name

class PersonDATA(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    summary = models.TextField()
    contact_number = models.CharField(max_length=16)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
