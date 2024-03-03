from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse("About page")


