from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path("add/", views.TaskCreateView.as_view(), name="task_add"),
    path("<int:pk>/", views.TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete", views.TaskDeleteView.as_view(), name="task_delete"),
    path("<int:pk>/set-done", views.TaskSetDoneView.as_view(), name="task_set_done"),
]
