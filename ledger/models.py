from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField(validators=[MinLengthValidator(50, 'the field must contain at least 50 characters')])


class Ingredient(models.Model):
    name = models.CharField(max_length=101)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.pk)])


class Recipe(models.Model):
    name = models.CharField(max_length=101)
    author = models.CharField(max_length=101, default='Author Name')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=101)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredients')
