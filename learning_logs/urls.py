"""Define schemas URL for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topic/', views.topics, name='topics'),
    path('topics/<int:topic_id>', views.topic, name='topic'),
    ]