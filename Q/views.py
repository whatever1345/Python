from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import NewQuestForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Q(request):
    questions = Question.objects.all()
    return render(request, 'question.html', {'questions': questions})

def detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, 'detail.html', {'question':question})

@login_required
def new(request):
    if request.method == "POST":
        form = NewQuestForm(request.POST)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.starter = request.user
            quest.save()
            return redirect('question:detail', slug=quest.slug)
    else:
        form = NewQuestForm()

    return render(request, 'new.html', {'form': form})


