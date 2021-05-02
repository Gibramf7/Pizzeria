import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()


for pizza in pizzas:
    print(pizza.id, pizza)

toppings = Topping.objects.all()
for t in toppings:
    print(f"Pizza: {t.pizza}")
    print(f"Name: {t}")
    print(f"Date Added: {t.date_added}")

'''
toppings = n.topping_set.all()

for topping in toppings:
    print(topping)
'''