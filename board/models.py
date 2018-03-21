from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(default="content")
    description = models.CharField(max_length=150, default="desc")
    genre = models.ManyToManyField(Genre, related_name="topics")
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

class Comment(models.Model):
    message = models.TextField(default="message")
    topic = models.ForeignKey(Topic, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="comments", on_delete=models.SET_NULL, null=True)



