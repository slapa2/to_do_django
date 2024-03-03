from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Task


class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = ['name']

