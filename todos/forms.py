from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "priority", "due_date"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "What needs to be done?"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input form-textarea",
                    "placeholder": "Add details (optional)",
                    "rows": 3,
                }
            ),
            "priority": forms.Select(attrs={"class": "form-input"}),
            "due_date": forms.DateInput(
                attrs={"class": "form-input", "type": "date"}
            ),
        }
