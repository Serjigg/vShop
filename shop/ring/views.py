from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

MENU = [{'title': 'Главная', 'url_name': 'start_page'},
        {'title': 'Каталог', 'url_name': 'start_page'},
        {'title': 'Бренды', 'url_name': 'sources'},
        {'title': 'Отзывы', 'url_name': 'start_page'},
        {'title': 'Контакты', 'url_name': 'start_page'},
        ]


def main(request):
    print('start_pahe')
    #return render(request, "ring/start_page.html", )
    return render(request, 'ring/start_page.html', { 'form': "form", 'menu': MENU})


def sources(request):
    return render(request, 'ring/sources.html')