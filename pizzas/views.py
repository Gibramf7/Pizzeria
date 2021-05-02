from django.shortcuts import render, redirect

from .models import Pizza
from .forms import PizzaForm

# Create your views here.


def index(request):
    '''The home page for Pizzeria. '''
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.order_by('-date_added')
    comments = pizza.comment_set.order_by('-date_added')

    context = {'pizza': pizza, 'toppings': toppings, 'comments': comments}

    return render(request, 'pizzas/pizza.html', context)


def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()

    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():

            new_pizza = form.save(commit=False)

            new_pizza.save()

            return redirect('pizzas:pizza')

    context = {'form': form}
    return render(request, 'pizzas/new_pizza.html', context)