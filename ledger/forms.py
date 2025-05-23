from django import forms
from django.contrib.auth.models import User

from .models import Recipe


class RecipeCreateForm(forms.ModelForm):
    """Create a form to Create a Recipe."""

    class Meta:
        model = Recipe
        fields = ['name']
