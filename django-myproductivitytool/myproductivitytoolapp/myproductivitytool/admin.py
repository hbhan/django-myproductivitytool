from django.contrib import admin
from . import models


class TaskListAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "deadline_date")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.TaskList, TaskListAdmin)
admin.site.register(models.Project, ProjectAdmin)
