from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

def RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"

def RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"