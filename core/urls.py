from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=views.index),
    path('user/', view=include('user.urls')),
    path('question/', view=include('question.urls')),
]
