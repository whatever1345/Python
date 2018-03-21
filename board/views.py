from django.shortcuts import render, get_object_or_404
from .models import Topic

# Create your views here.


def index(request):
    topics = Topic.objects.all()
    return render(request, 'index.html', {'topics': topics})


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render(request, 'topic.html', {'topic':topic})

