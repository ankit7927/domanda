from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class TagModel(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self) -> str:
        return self.name

class QuestionModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(TagModel, blank=True)
    slug = models.SlugField(max_length=40, unique=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    
    def save(self, **kwargs) -> None:
        self.slug = slugify(self.title+" "+self.content[:20])
        return super(QuestionModel, self).save(**kwargs)


class AnswerModel(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.content[:30]


