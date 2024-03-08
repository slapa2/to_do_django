from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Task
from .forms import SetDoneForm


class TaskListView(LoginRequiredMixin, ListView):
    queryset = Task.objects.order_by('done', '-updated')
    context_object_name = "task_list"

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        set_done_form = SetDoneForm()
        context['active'] = 'task-list'
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['active'] = 'task-add'
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["name"]

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['active'] = 'task-list'
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")


class TaskSetDoneView(LoginRequiredMixin, View):

    form = SetDoneForm

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
            task.done = True
            task.save()
        return HttpResponseRedirect(reverse_lazy("task-list"))
