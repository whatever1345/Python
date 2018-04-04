from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import NewQuestForm, PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Q(request):
    questions = Question.objects.all()
    return render(request, 'question.html', {'questions': questions})

def detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = PostForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.question = question
                post.created_by = request.user
                post.save()
                return redirect('question:detail', slug=question.slug)
        else:
            return redirect('accounts:login')
    return render(request, 'detail.html', {'question':question, 'form':form})

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


