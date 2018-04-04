from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from .models import Topic
from .forms import CommentForm

# Create your views here.


def index(request):
    topics = Topic.objects.all()
    return render(request, 'index.html', {'topics': topics})


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    topic.views += 1
    topic.save()
    form = CommentForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.topic = topic
                comment.created_by = request.user
                comment.save()
                return redirect('board:topic_detail', slug=topic.slug)
        else:
            return redirect('accounts:login')
    return render(request, 'topic.html', {'topic':topic, 'form':form})


class TopicViews(View):
    def render(self, request, slug):
        topic = get_object_or_404(Topic, slug=slug)
        topic.views += 1
        topic.save()
        return render(request, 'topic.html', {'topic':topic, 'form': self.form})

    @method_decorator(login_required)
    def post(self, request, slug):
        self.form = CommentForm(request.POST)
        if self.form.is_valid():
            self.form.topic = self.topic
            self.form.created_by = self.request.user
            self.form.save()
        return self.render(request, slug=slug)

    def get(self, request, slug):
        self.form = CommentForm()
        return self.render(request, slug)

