from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)

class RecipeIngredient(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)