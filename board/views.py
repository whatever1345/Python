from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import Topic, Comment
from .forms import CommentForm

# Create your views here.


def index(request):
    topics = Topic.objects.all()
    return render(request, 'index.html', {'topics': topics})


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.created_by = request.user
            comment.save()
            return redirect('board:topic_detail', slug=topic.slug)
    else:
        form = CommentForm()
    return render(request, 'topic.html', {'topic':topic, 'form':form})




