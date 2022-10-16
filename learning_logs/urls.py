from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topic/', views.topics, name='topics'),
    path('topics/<int:topic_id>', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    #The page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #The page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
    ]