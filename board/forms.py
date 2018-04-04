from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': 'Your answer here'}
        ),
    )

    class Meta:
        model = Comment
        fields = ['message', ]