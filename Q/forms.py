from django import forms
from .models import Question

class NewQuestForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Give a brief explanation to your question'}
        ),
    )

    class Meta:
        model = Question
        fields = ['question', 'message']