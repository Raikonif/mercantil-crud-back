from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CommentForm, TaskForm
from .models import Comment, Task


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "core/task_list.html"


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "core/task_detail.html"

    def get_queryset(self):
        return Task.objects.prefetch_related("comments")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = kwargs.get("comment_form", CommentForm())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.task = self.object
            form.save()
            return redirect("task-detail", pk=self.object.pk)
        return self.render_to_response(self.get_context_data(comment_form=form))


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "core/task_form.html"

    def get_success_url(self):
        return reverse("task-detail", kwargs={"pk": self.object.pk})


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "core/task_form.html"

    def get_success_url(self):
        return reverse("task-detail", kwargs={"pk": self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("task-list")
    template_name = "core/task_confirm_delete.html"


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "core/comment_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=kwargs["task_pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.task = self.task
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = self.task
        return context

    def get_success_url(self):
        return reverse("task-detail", kwargs={"pk": self.task.pk})


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    context_object_name = "comment"
    template_name = "core/comment_form.html"

    def get_queryset(self):
        return Comment.objects.select_related("task")

    def get_success_url(self):
        return reverse("task-detail", kwargs={"pk": self.object.task_id})


class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = "comment"
    template_name = "core/comment_confirm_delete.html"

    def get_queryset(self):
        return Comment.objects.select_related("task")

    def get_success_url(self):
        return reverse("task-detail", kwargs={"pk": self.object.task_id})
