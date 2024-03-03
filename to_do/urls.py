from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list-view'),
    path("add/", views.TaskCreateView.as_view(), name="task-add"),
]
