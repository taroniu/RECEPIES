from stations.views import bus_stations
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def dish_view(request, dish):
    if dish == 'busstations':
        return bus_stations(request)
    else:
    # dish = request.GET['dish']
        servings = int(request.GET.get('servings', 1))
        context = {}
        for i in DATA[dish]:
            context[i] = DATA[dish][i] * servings
        return HttpResponse(f'{i}: {context[i]}<br>' for i in context)