from django.shortcuts import render
from .models import TipoIngrediente, TipoPizza, Ingrediente, Pizza, IngredientePizza

# Create your views here.
def home(request):
    """Pagina Incial"""
    pizzas_salgadas = Pizza.objects.filter(tipo_pizza_nome="Salgada", ativa=True)
    pizzas_doces = Pizza.objects.filter(tipo_pizza_nome="Doce", ativa=True)

    #Dicionario com os dadso que eu quero mostrar na tela
    context = {
        "pizzas_salgadas" : pizzas_salgadas,
        "pizzas_doces" : pizzas_doces
    }
    
    #Renderizar - mostrar na tela
    return render(request, 'cardapio/home.html', context)