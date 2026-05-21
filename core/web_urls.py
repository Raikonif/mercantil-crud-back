from django.urls import path

from .views import (
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/new/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:task_pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path(
        "comments/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment-delete",
    ),
]
