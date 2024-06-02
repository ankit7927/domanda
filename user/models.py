from django.db import models
from django.contrib.auth.models import User
from question.models import QuestionModel

class ProfileModel(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    pic = models.ImageField(upload_to="media/pics", null=True, blank=True)
    liked_questions = models.ManyToManyField(to=QuestionModel, blank=True)

    def __str__(self) -> str:
        return self.name
