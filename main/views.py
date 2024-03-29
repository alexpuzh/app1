from django.shortcuts import render
from django.shortcuts import HttpResponse

from goods.models import Categories


def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст который описывает магазин'

    }
    return render(request, 'main/about.html', context)


