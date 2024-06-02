from django.shortcuts import render
from question.models import QuestionModel, TagModel


def index(request):
    questions = QuestionModel.objects.all()
    tags = TagModel.objects.all()
    return render(request=request, template_name="index.html", context={"questions":questions[1:], "latest": questions[0], "tags":tags})


def notfound(request):
    return render(request=request, template_name="notfound.html")
