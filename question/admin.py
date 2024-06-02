from django.contrib import admin
from .models import AnswerModel, QuestionModel, TagModel

admin.site.register((AnswerModel, QuestionModel, TagModel))
