from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'to_do/index.html', context)
