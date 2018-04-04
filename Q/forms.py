from django import forms
from .models import Question, Post


class NewQuestForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Give a brief explanation to your question'}
        ),
    )

    class Meta:
        model = Question
        fields = ['question', 'message']


class PostForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': 'Your answer here'}
        ),
    )

    class Meta:
        model = Post
        fields = ['message', ]
