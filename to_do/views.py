from django.shortcuts import render
from django.views import View
from .models import Task


class Home(View):

    def get(self, request):
        qs = Task.objects.all()
        context = {
            'qs': qs,
        }
        return render(request, 'to_do/index.html', context)
