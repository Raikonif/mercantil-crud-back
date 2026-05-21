from django import forms
from django.utils import timezone

from .models import Comment, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "limit_date"]
        widgets = {
            "limit_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_title(self) -> str:
        title = self.cleaned_data["title"]
        if len(title.strip()) < 5:
            raise forms.ValidationError("Title must contain at least 5 characters.")
        return title

    def clean_limit_date(self):
        limit_date = self.cleaned_data["limit_date"]
        if limit_date < timezone.localdate():
            raise forms.ValidationError(
                "Limit date cannot be less than the current date."
            )
        return limit_date


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 4}),
        }
