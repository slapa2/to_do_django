from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path("add/", views.TaskCreateView.as_view(), name="task-add"),
    path("<int:pk>/", views.TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete", views.TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/set-done", views.TaskSetDoneView.as_view(), name="task-set-done"),
]
