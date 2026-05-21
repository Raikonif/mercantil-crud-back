from django.contrib import admin

from .models import Comment, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "priority", "limit_date", "created_at"]
    list_filter = ["status", "priority", "limit_date"]
    search_fields = ["title", "description"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["task", "comment", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["comment", "task__title"]
