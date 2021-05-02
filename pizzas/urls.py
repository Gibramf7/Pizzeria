from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    #path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    #path('new_pizza/', views.new_pizza, name='new_pizza'),
    #path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping'),
    #path('edit_topping/<int:topping_id>',
         #views.edit_topping, name='edit_topping'),
    #path('new_comment/<int:pizza_id>', views.new_comment, name='new_comment'),

]