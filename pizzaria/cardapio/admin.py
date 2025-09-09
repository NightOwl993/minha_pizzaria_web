from django.contrib import admin
from django.utils.html import format_html
from .models import TipoIngrediente, TipoPizza, Ingrediente, Pizza, IngredientePizza
# Register your models here.

@admin.register(TipoPizza)
class TipoPizzaAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao']

@admin.register(TipoIngrediente)
class TipoIngredienteAdmin(admin.ModelAdmin):
    list_display=['nome', 'tipo_ingrediente', 'preco_formatado', 'disponivel']

#Filtros
list_filter = ['tipo_ingrediente', 'disponivel']

def preco_formatado(self,obj):
    return f'R$ {obj.preco_por_unidade:.3f}/{obj.unidade_medida}'

#Rotulo
preco_formatado.short_description = 'Preço'