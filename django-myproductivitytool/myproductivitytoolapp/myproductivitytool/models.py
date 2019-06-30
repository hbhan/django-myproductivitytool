from django.utils import timezone
from django.db import models


class Project(models.Model):  # The Project table name that inherits models.Model
    objects = models.Manager()
    name = models.CharField(max_length=100)  # Like a varchar

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name  # name to be shown when called


class TaskList(models.Model):  # Tasklist able name that inherits models.Model
    objects = models.Manager()
    title = models.CharField(max_length=250)  # a varchar
    content = models.TextField(blank=True)  # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    deadline_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default="general")  # a foreignkey

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called
