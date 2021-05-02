from django.shortcuts import render

from .models import Pizza

# Create your views here.


def index(request):
    '''The home page for Pizzeria. '''
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)