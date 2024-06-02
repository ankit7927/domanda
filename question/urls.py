from django.urls import path
from . import views


urlpatterns = [
    path("new", view=views.new_question, name="new"),
    path("edit/<int:questionId>", view=views.edit_question, name="edit"),
    path("delete/<int:questionId>", view=views.delete_question, name="delete"),
    path("get", view=views.get_questions, name="get"),
    path("get/<slug:slug>", view=views.get_questions, name="get"),
    path("answer/<int:questionId>", view=views.new_answer, name="nw ans"),
    path("answer/<int:answerId>/delete", view=views.delete_answer, name="del ans"),

    path("likedis/<int:questionId>", view=views.like_dislike_question, name="like dis"),
]