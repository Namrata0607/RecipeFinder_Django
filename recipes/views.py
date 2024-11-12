# recipes/views.py
from django.shortcuts import render
from .utils import get_recipes

def recipe_search(request):
    recipes = None
    if 'ingredient' in request.GET:
        ingredient = request.GET['ingredient']
        recipes = get_recipes(ingredient)
    return render(request, 'recipes/search.html', {'recipes': recipes})

def recipe_list(request):
    return render(request, 'recipes/recipe_list.html')