from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe
from .forms import RecipeCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
    redirect_field_name = 'recipes/list'

@login_required
def RecipeAddView(request):
    recipe_form = RecipeCreateForm()
    if request.method == 'POST':
        recipe_form = RecipeCreateForm(request.POST)
        if recipe_form.is_valid:
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user.profile.name
            recipe.save()
            return redirect('/recipes/list', pk=recipe.pk)
    ctx = {
        "recipe_form": recipe_form,
    }
    return render(request, 'recipe_add.html', ctx)

    
class ImageAddView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "image_add.html"
    redirect_field_name = 'recipe/pk/add_image'