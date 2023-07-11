from django import forms
from .models import Review


class CommentsAddForm(forms.ModelForm):
    # Adding a comment
    class Meta:
        model = Review
        fields = (
            'name', 'text', 'email'
        )