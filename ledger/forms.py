from django import forms
from django.contrib.auth.models import User

from .models import Recipe, RecipeImage


class RecipeCreateForm(forms.ModelForm):
    """Create a form to Create a Recipe."""

    class Meta:
        model = Recipe
        fields = ['name']

class ImageAddForm(forms.ModelForm):
    """Create a form to Create a Recipe."""

    class Meta:
        model = RecipeImage
        fields = ['image','description']
