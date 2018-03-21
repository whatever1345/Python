from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=255)
    message = models.TextField(default="message")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True, default="content")
    starter = models.ForeignKey(User, related_name='questions', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(Question, self).save(*args, **kwargs)

class Post(models.Model):
    message = models.TextField(default="message")
    question = models.ForeignKey(Question, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.SET_NULL, null=True)